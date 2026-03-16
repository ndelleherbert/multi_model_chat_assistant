import os
import streamlit as st
import anthropic
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_secret(key):
    return os.getenv(key) or st.secrets.get(key)

# ── Available Models ──────────────────────────────────────
MODELS = {
    "DeepSeek Chat":     {"provider": "deepseek",  "model_id": "deepseek-chat"},
    "DeepSeek Reasoner": {"provider": "deepseek",  "model_id": "deepseek-reasoner"},
    "Claude Sonnet":     {"provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
    "Claude Haiku":      {"provider": "anthropic", "model_id": "claude-haiku-4-5-20251001"},
}

# ── Available Languages ───────────────────────────────────
LANGUAGES = [
    "English", "French", "Spanish", "Arabic", "Chinese",
    "German", "Portuguese", "Japanese", "Korean", "Hindi",
    "Italian", "Russian", "Turkish", "Dutch", "Swahili"
]

def get_deepseek_client():
    return OpenAI(
        api_key=get_secret("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )

def get_anthropic_client():
    return anthropic.Anthropic(api_key=get_secret("ANTHROPIC_API_KEY"))

def get_response(messages, model_name, temperature=0.7, max_tokens=1024, language="English"):
    config = MODELS[model_name]
    provider = config["provider"]
    model_id = config["model_id"]

    # ✅ Inject language instruction as system message
    system_message = f"You are a helpful assistant. Always respond in {language}."

    if provider == "deepseek":
        client = get_deepseek_client()
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "system", "content": system_message}] + messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

    elif provider == "anthropic":
        client = get_anthropic_client()
        filtered = [m for m in messages if m["role"] != "system"]
        response = client.messages.create(
            model=model_id,
            max_tokens=max_tokens,
            system=system_message,
            messages=filtered
        )
        return response.content[0].text

    else:
        raise ValueError(f"Unknown provider: {provider}")