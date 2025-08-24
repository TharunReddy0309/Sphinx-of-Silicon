# 🔮 The Sphinx of Silicon

An interactive **Streamlit riddle game** powered by **LangChain** and **Groq LLMs**.  
Solve riddles to gradually reveal a hidden poetic phrase, guarded by the mysterious Sphinx.  
Hints are generated dynamically using a custom-trained linear regression model.

---

## 📂 Project Structure
.
├── game.py # Main Streamlit app (riddle game)
├── kmodel.py # Linear regression model for hint difficulty
├── linearmodel.joblib # Saved trained regression model
├── requirements.txt # Project dependencies

yaml
Copy
Edit

---

## 🚀 Features
- 🎭 **AI-generated secret phrase** based on a random theme  
- 🧩 **Riddle challenges** where each correct answer reveals a word of the phrase  
- 💡 **Dynamic hint system** powered by a trained linear regression model (`kmodel.py`)  
- 🧠 **Conversational AI** (Groq LLM via LangChain) responds to wrong answers and provides hints  
- 🎉 Unlock the **full secret phrase** with celebratory balloons & effects in Streamlit  

---

## 🛠 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sphinx-riddle-game.git
cd sphinx-riddle-game
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
# Activate on Linux/Mac
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up environment variables
Create a .env file in the project root with your Groq API key:

ini
Copy
Edit
groqai=your_api_key_here
▶️ Running the Game
bash
Copy
Edit
streamlit run game.py
Open the local URL from the terminal (default: http://localhost:8501).

🧮 How Hint Difficulty Works
The kmodel.py trains a simple linear regression model with scikit-learn.
The model predicts a difficulty score based on:

a → Number of riddles solved so far

b → Number of hints requested

Score Range	Hint Type
< 30	Small hint
30–65	Medium hint
65–80	Big hint
> 80	Full answer (game loss)

🛠 Tech Stack
Python 3.12.0

Streamlit → Interactive UI

LangChain → Conversational AI orchestration

Groq LLMs → AI-powered riddles, phrases, and hints

scikit-learn → Linear regression model

NumPy → Numerical operations

Joblib → Model persistence

python-dotenv → Environment management

📦 Requirements
Main dependencies (see requirements.txt):

streamlit

python-dotenv

langchain

langchain-groq

scikit-learn

numpy

joblib

✨ Future Improvements
Add difficulty levels (easy/medium/hard riddles)

Support multiplayer mode

Save game progress in a database

Theming and UI improvements

👤 Author
Tharun