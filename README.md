# 🤖 VibeChat – Mood-Based Chatbot

VibeChat is an interactive AI chatbot that responds based on different emotional modes.
Users can choose how the chatbot behaves — Angry 😡, Funny 😂, or Sad 😢 — and get responses in that specific tone.

---

## 🚀 Features

* 🎭 Multiple chatbot personalities:

  * Angry Mode 😡
  * Funny Mode 😂
  * Sad Mode 😢
* 💬 Interactive chat UI using Streamlit
* 🧠 Powered by Mistral AI (via LangChain)
* 🖥️ CLI-based chatbot support
* 🔐 Secure environment variable handling using `.env`

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* LangChain
* Mistral AI API
* dotenv

---

## 📁 Project Structure

```
├── app.py                # Streamlit UI chatbot
├── chatbot.py       # Terminal-based chatbot
├── .env                 # Environment variables (API key)
├── requirements.txt     # Dependencies
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/mood-based-chatbot.git
cd mood-based-chatbot
```

---

### 2️⃣ Create virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file in the root directory and add:

```
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

### 🔹 Run Streamlit UI

```
streamlit run app.py
```

---

### 🔹 Run CLI Chatbot

```
python chatbot.py
```

---

## 🎮 How It Works

1. Select a chatbot mode:

   * Angry 😡 → Aggressive responses
   * Funny 😂 → Humorous replies
   * Sad 😢 → Emotional tone

2. Enter your message

3. Chatbot responds based on selected mood

---

## 📸 Demo

*(Add screenshots here if needed)*

---

## 💡 Future Improvements

* Add more moods (Happy, Sarcastic, Motivational)
* Voice-based interaction
* Chat history saving
* Deploy on cloud (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Sikun Kumar Rout**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
