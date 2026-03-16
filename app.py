import streamlit as st
from utils.model_utils import get_response, MODELS, LANGUAGES

st.set_page_config(page_title="Herbert's Multi-Model Chat Assistant", page_icon="🤖")
st.title("🤖 Multi-Model Chat Assistant")

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")

    # Model name selector
    selected_model = st.selectbox("🤖 Model Name", list(MODELS.keys()))

    # Model ID (read-only display + selectable)
    model_id = MODELS[selected_model]["model_id"]
    st.text_input("🔖 Model ID", value=model_id, disabled=True)

    # Language selector
    selected_language = st.selectbox("🌍 Response Language", LANGUAGES)

    st.divider()

    temperature = st.slider("🌡️ Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.slider("📏 Max Tokens", 256, 4096, 1024, 256)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ── Chat History ──────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Regenerate Button ─────────────────────────────────────
if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
    if st.button("🔄 Regenerate"):
        st.session_state.messages.pop()
        with st.chat_message("assistant"):
            with st.spinner(f"Regenerating with {selected_model} in {selected_language}..."):
                response = get_response(
                    messages=st.session_state.messages,
                    model_name=selected_model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    language=selected_language
                )
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# ── Chat Input ────────────────────────────────────────────
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner(f"Thinking with {selected_model} in {selected_language}..."):
            response = get_response(
                messages=st.session_state.messages,
                model_name=selected_model,
                temperature=temperature,
                max_tokens=max_tokens,
                language=selected_language
            )
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})