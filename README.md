# 🤖 Multi-Model Chat Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![LLM](https://img.shields.io/badge/LLM-OpenAI%20%7C%20Gemini-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project-Active-success)

An interactive AI chat application that behaves like **ChatGPT** and supports **multiple Large Language Model providers** including **OpenAI** and **Google Gemini**.

The application maintains conversation context, allows users to regenerate responses, and provides quick copy functionality for generated answers.

---

# 📌 Project Overview

The **Multi-Model Chat Assistant** is designed to demonstrate how modern AI chat systems work internally.

This project shows how to:

* Connect to multiple LLM providers
* Maintain conversation history
* Manage chat memory
* Implement response regeneration
* Provide copy functionality for AI responses

Users can send questions and receive responses from different AI models while maintaining the context of the conversation.

---

# ✨ Features

## 🧠 Conversation Memory

The chatbot stores conversation history in a **list-based memory structure**.

Example:

```python
conversation_history = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help you today?"}
]
```

Each new message is appended to this list so the model can understand the **previous conversation context**.

---

## 🔁 Regenerate Response

The **Regenerate** button allows the user to generate a new answer for the last question.

How it works:

1. The previous AI response is removed from memory
2. The last user message remains
3. The model is called again
4. A new response is generated

This allows users to receive **alternative answers** without typing the question again.

---

## 📋 Copy Response

The **Copy** feature allows users to copy AI-generated responses instantly.

When the copy button is clicked:

* The response text is copied to the clipboard
* Users can paste it anywhere (documents, notes, code editors)

---

## 🔄 Multi-Model Support

Users can switch between different AI providers.

Supported providers:

* **OpenAI**
* **Google Gemini**

This allows users to compare responses from different models.

---

# 🧩 Supported Models

### OpenAI

* GPT-4
* GPT-4o
* GPT-4o-mini

### Google Gemini

* Gemini 1.5 Pro
* Gemini 1.5 Flash

---

# 🛠️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/multi-model-chat-assistant.git
cd multi-model-chat-assistant
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv myvenv
```

Activate environment.

### Windows

```bash
myvenv\Scripts\activate
```

### Mac/Linux

```bash
source myvenv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure API Keys

Create environment variables for your API keys.

Example:

```
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## 5️⃣ Run the Application

```bash
python app.py
```

The chat interface will start and you can begin interacting with the assistant.

---

# 📂 Project Structure

```
multi-model-chat-assistant
│
├── app.py
├── requirements.txt
├── README.md
│
├── models
│   ├── openai_model.py
│   └── gemini_model.py
│
├── memory
│   └── conversation_memory.py
│
└── utils
    └── helpers.py
```

---

# 🧑‍💻 Technologies Used

* Python
* OpenAI API
* Google Gemini API
* List-based memory management
* Virtual environments
* REST API calls

---

# 🚀 Future Improvements

Possible improvements for the project:

* Chat history database storage
* Streaming responses
* Voice chat integration
* User authentication
* Web interface (Streamlit / React / Flask)
* File uploads and document Q&A

---

# 📸 Screenshots

*(Add screenshots of the chat interface here)*

Example:

```
![Chat UI](screenshots/chat_ui.png)
```

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Ndelle Njumbe Sekinah Herbert**

AI & Software Development Enthusiast
