# 🧠 Friday – AI Voice Assistant in Python

Friday is a voice-controlled AI assistant built using Python. It responds to spoken commands, opens websites, fetches the current time, translates text, and even answers general questions using **Google Gemini AI (Gemini 1.5 Flash)**.

---

## 🚀 Features

- 🎙️ Voice activation ("Friday")
- 🌐 Open popular websites like Google, YouTube, Facebook
- 🕒 Tell the current time
- 🔍 Perform Google searches
- 🧠 Ask anything using Google Gemini AI API (like ChatGPT)
- 💬 Text-to-speech responses for all actions

---

## 🛠️ Tech Stack

- **Python 3.10+**
- `speechrecognition` – for voice input
- `pyttsx3` – for text-to-speech output
- `webbrowser` – to open websites
- `googlesearch-python` – for web search
- `google-generativeai` – Gemini API access
- `And Some more for all package check requirements.txt`

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/AniketKumar15/PythonCodes
   cd PythonCodes/Assistant
   ```
2. **Create and activate virtual environment (optional but recommended)**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set your Gemini API Key**
    - Replace API_KEY in the script with your own Gemini key:
        ```bash
        API_KEY = "your-api-key-here"
        ```
5. **Run the assistant**
    ```bash
    python main.py
    ```
---

## 🎤 Usage
- Say `"Friday"` to activate.
- Then say commands like:
    - `"Open Google"`
    - `"What is the current time?"`
    - `"Translate good morning"`
    - `"Search how to make chocolate cake"`
    - `"Gemini what is quantum computing"`
    - `"Stop" or "Go offline" to exit.`

---

## 🧠 Credits
- CodeWithHarry Python Course
- Google Generative AI (Gemini)
- Python Community Libraries

---

## 🙋‍♂️ Author
- **Aniket Kumar**
- **Game Developer turned Python Explorer**
- **GitHub: [@AniketKumar15](https://github.com/AniketKumar15)**
