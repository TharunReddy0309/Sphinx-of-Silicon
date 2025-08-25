import os
import json
import random
from dotenv import load_dotenv
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
import themes
import linmodel

# ---------------- Setup ----------------
load_dotenv()

chat_model_groq = ChatGroq(
    groq_api_key=st.secrets["groqai"],
    temperature=0.9,
    model_kwargs={"top_p": 0.9},
    model="openai/gpt-oss-120b"  
)

# ---------------- Generate Secret Phrase ----------------
if "game_state" not in st.session_state:
    chosen_theme = themes.x()

    prompt = f"""
    Give me a poetic, meaningful phrase of 5–7 words,
    like an ancient proverb or mystical wisdom.
    The theme is **{chosen_theme}**.
    No explanation, just the phrase.
    """
    result = chat_model_groq.invoke(prompt)
    secret_phrase = result.content.strip()
    secret_words = secret_phrase.split()

    # generate riddles
    prompt_riddles = f"""
    Generate {len(secret_words)} simple different riddles with answer most related to the meaning of {secret_phrase} in JSON format.
    Each riddle must have "q" (question) and "a" (answer).  
    Answers must all be unique.  
    Output a JSON list of length {len(secret_words)}.  
    Example:
    [{{"q":"I speak without a mouth...","a":"echo"}}]
    """
    result_riddles = chat_model_groq.invoke(prompt_riddles)

    try:
        riddles = json.loads(result_riddles.content)
    except:
        st.error("⚠️ Could not parse riddles, using fallback.")
        riddles = [{"q": "I am always hungry but never eat. What am I?", "a": "fire"}]
    print(riddles)
    # Store in session
    st.session_state.game_state = {
        "secret_phrase": secret_phrase,
        "secret_words": secret_words,
        "riddles": riddles,
        "solved_riddles": 0,
        "revealed_words": [],
        "x": 0,  # hint difficulty counter
        "y": 1,
        'z':0
    }
    st.session_state.messages = [
        SystemMessage(content="""
        You are **The Sphinx of Silicon**, guardian of secrets.
        Rules:
        1. Do not reveal the secret phrase directly (unless all riddles are solved).
        2. Only reveal one word when the user solves a riddle.
        3. Encourage, give hints, but stay mysterious.
        """)
    ]

st.title("🔮 The Sphinx of Silicon")
st.caption("Solve riddles to reveal the hidden phrase.")

game = st.session_state.game_state
messages = st.session_state.messages

# Show revealed words
if game["revealed_words"]:
    st.success("✨ Revealed words so far: " + " ".join(game["revealed_words"]))

# If all riddles are solved → Reveal final phrase
if game["solved_riddles"] >= len(game["riddles"]):
    st.balloons()
    st.success(f"🎉 You unlocked the full secret phrase: **{game['secret_phrase']}**")
    st.stop()

# Otherwise → Show next riddle
riddle = game["riddles"][game["solved_riddles"]]
st.markdown(f"**Riddle {game['solved_riddles']+1}/{len(game['riddles'])}:** {riddle['q']}")

# ---------------- Chat Input ----------------
user_input = st.chat_input("Your Answer (or type 'hint')")

if user_input:
    user_input = user_input.strip().lower()

    if user_input in ["exit", "quit", "bye"]:
        st.write("👋 The Sphinx vanishes into the mist...")
        st.stop()

    # ✅ Correct answer → Unlock next word + move to next riddle
    if user_input == riddle["a"].lower():
        game["solved_riddles"] += 1
        next_word = game["secret_words"][game["solved_riddles"] - 1]
        game["revealed_words"].append(next_word)
        game["y"] += 1
        game["x"] = 0
        st.success(f"✅ Correct! You unlocked a secret word: **{next_word}**")

        # 🔁 After answering, show next riddle immediately
        if game["solved_riddles"] < len(game["riddles"]):
            next_riddle = game["riddles"][game["solved_riddles"]]
            st.markdown(f"**Next Riddle:** {next_riddle['q']}")
        else:
            if game['z']!=0:
                st.warning("😈 You have lose the game Mortal")
            else:
                st.balloons()
                st.success(f"🎉 You unlocked the full secret phrase: **{game['secret_phrase']}**")

    # Hint request
    elif user_input == "hint":
        game["x"] += 1
        level = linmodel.p(game["y"], game["x"])
        if level < 30:
            hint_level = "small"
        elif level <= 65:
            hint_level = "medium"
        elif level <= 80:
            hint_level = "big"
        else:
            st.info(f"🗝️ The answer is: **{riddle['a']}**")
            game['z']+=1
            st.stop()

        seed = random.randint(1000, 9999)
        prompt = f"""
        You are the Sphinx. Provide a {hint_level} hint for this riddle: "{riddle['q']}".
        Seed {seed} ensures variety.
        """
        response = chat_model_groq.invoke(prompt)
        st.info("💡 Hint: " + response.content.strip())

    # Wrong answer → Encourage
    else:
        messages.append(HumanMessage(content=f"The user answered '{user_input}', but it is wrong. Encourage them."))
        response = chat_model_groq.invoke(messages)
        st.warning("🌀 " + response.content.strip())
        messages.append(AIMessage(content=response.content))
