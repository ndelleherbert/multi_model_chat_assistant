import streamlit as st
from openai import OpenAI
import google.generativeai as genai
import os
from dotenv import load_dotenv
import pyperclip

# Load API keys
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

# Configure models
openai_client = OpenAI(api_key=openai_key)
genai.configure(api_key=gemini_key)

# Streamlit title
st.title("Ndelle Herbert's Multi-Model Chat Assistant")

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar settings
st.sidebar.header("Settings")

provider = st.sidebar.selectbox(
    "Choose Model Provider",
    ["OpenAI", "Gemini"]
)

language = st.sidebar.selectbox(
    "Output Language",
    ["English", "Hindi"]
)

memory_window = st.sidebar.slider(
    "Memory Window",
    1,
    10,
    5
)

# Model selection
if provider == "OpenAI":
    model = st.sidebar.selectbox(
        "OpenAI Models",
        ["gpt-4o-mini", "gpt-4o"]
    )

else:
    model = st.sidebar.selectbox(
        "Gemini Models",
        ["gemini-1.5-flash", "gemini-1.5-pro"]
    )


# Display chat history
for i, msg in enumerate(st.session_state.messages):

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

        if msg["role"] == "assistant":
            if st.button("Copy", key=i):
                pyperclip.copy(msg["content"])
                st.success("Copied!")


# Chat input
user_input = st.chat_input("Ask something...")

if user_input:

    # store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # memory window
    memory = st.session_state.messages[-memory_window:]

    system_prompt = f"Answer strictly in {language}"

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(memory)

    # Generate response
    if provider == "OpenAI":

        response = openai_client.chat.completions.create(
            model=model,
            messages=messages
        )

        reply = response.choices[0].message.content

    else:

        gemini_model = genai.GenerativeModel(model)

        prompt = "\n".join([m["content"] for m in messages])

        result = gemini_model.generate_content(prompt)

        reply = result.text

    # save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)


# Regenerate response
if st.button("Regenerate Response"):

    if len(st.session_state.messages) >= 2:

        # remove last assistant message
        if st.session_state.messages[-1]["role"] == "assistant":
            st.session_state.messages.pop()

        # find last user message
        last_user = None
        for msg in reversed(st.session_state.messages):
            if msg["role"] == "user":
                last_user = msg["content"]
                break

        memory = st.session_state.messages[-memory_window:]

        system_prompt = f"Answer strictly in {language}"

        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(memory)

        if provider == "OpenAI":

            response = openai_client.chat.completions.create(
                model=model,
                messages=messages
            )

            reply = response.choices[0].message.content

        else:

            gemini_model = genai.GenerativeModel(model)

            prompt = "\n".join([m["content"] for m in messages])

            result = gemini_model.generate_content(prompt)

            reply = result.text

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        st.rerun()