# 🔮 The Sphinx of Silicon

> *"Answer wisely, mortal… for with each riddle solved, the Sphinx lets you peek at a hidden truth."*  

An interactive **AI-powered riddle game** built with **Streamlit**, **LangChain**, and **Groq LLMs**.  
Crack riddles to uncover a **mystical secret phrase** while the Sphinx tests your wit.  
Need help? A smart hint system powered by **machine learning** adjusts difficulty as you play.  
- **Here is the live link**- "sphinx-of-silicon.streamlit.app" search this in browser

---

## ✨ Why Play?
- 🧩 Solve fun, brain-teasing riddles  
- 🤖 Battle an **AI Sphinx** that reacts to your answers  
- 💡 Unlock **dynamic hints** (small → medium → big → full reveal)  
- 🎭 Reveal a **hidden poetic phrase** word by word  
- 🎉 Celebrate your victory with magical Streamlit effects  

It’s not just a game — it’s **AI + riddles + strategy** in one experience.  

---

## 📂 Project Structure
.
├── game.py # Main Streamlit app
├── kmodel.py # Linear regression model for hint difficulty
├── linearmodel.joblib # Trained regression model
├── requirements.txt # Dependencies


---

## 🚀 Quick Start
### 1. Clone the repo:
    ```bash
    git clone https://github.com/your-username/sphinx-riddle-game.git
    cd sphinx-riddle-game
2. Set up a virtual environment:

    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
3. Install dependencies:

    pip install -r requirements.txt
4. Add your API key:
    Create a .env file in the project root:
    groqai=your_api_key_here
5. Run the game:

    streamlit run game.py
    Open your browser → http://localhost:8501

How Hints Work
A linear regression model decides how big a hint you get:

Difficulty Score	What You See
    < 30	🪄 Small hint
    30–65	🔑 Medium hint
    65–80	🚪 Big hint
    > 80	💀 Full answer revealed → You lose!

The more riddles you solve and the more hints you request, the tougher it gets.

🛠 Tech Stack:
    
    Python 3.12.0
    
    Streamlit → UI & interactivity
    
    LangChain → Orchestrating the AI Sphinx
    
    Groq LLMs → Generating riddles & phrases
    
    scikit-learn → Hint difficulty model
    
    NumPy + Joblib → Data & model persistence
    
    python-dotenv → Environment config

📦 Requirements:
    streamlit

    python-dotenv
    
    langchain
    
    langchain-groq
    
    scikit-learn
    
    numpy
    
    joblib

(See requirements.txt for details.)

🛤 Roadmap / Future Magic
    ✨ Add difficulty modes (easy / medium / hard)
    ✨ Multiplayer Sphinx battles
    ✨ Save game progress in a database
    ✨ Themed riddles (mythology, sci-fi, fantasy)
    ✨ Richer UI with animations

👤 Author
    Tharun

Built with curiosity, code, and a love for riddles.
