# 🤖 Multi-Model Chat Assistant

A Streamlit chat app that lets you switch between **DeepSeek** and **Claude (Anthropic)** models in real time.

## ✨ Features
- 💬 Persistent chat history per session
- 🔀 Switch between DeepSeek and Claude models
- 🎛️ Configurable temperature and max tokens
- 🗑️ Clear chat button
- ☁️ Deployable on Streamlit Cloud

## 🚀 Getting Started

### 1. Clone the repo
\```bash
git clone <your-repo-url>
cd multi_model_chat_assistant
\```

### 2. Install dependencies
\```bash
pip install -r requirements.txt
\```

### 3. Set up environment
\```bash
cp .env.example .env
# Add your API keys to .env
\```

### 4. Run the app
\```bash
streamlit run app.py
\```

## ☁️ Streamlit Cloud Deployment

Add these in **Manage App → Settings → Secrets**:
\```toml
DEEPSEEK_API_KEY = "your_deepseek_key"
ANTHROPIC_API_KEY = "your_anthropic_key"
\```

## 🔑 API Keys
- DeepSeek: [platform.deepseek.com](https://platform.deepseek.com)
- Anthropic: [console.anthropic.com](https://console.anthropic.com)