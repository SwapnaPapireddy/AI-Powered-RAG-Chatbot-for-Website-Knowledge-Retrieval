import streamlit as st
import requests

# -----------------------------
# Streamlit Configuration
# -----------------------------
st.set_page_config(
    page_title="Website RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "website_loaded" not in st.session_state:
    st.session_state.website_loaded = False

# -----------------------------
# Header
# -----------------------------
st.title("🤖 Website RAG Chatbot")
st.markdown("Ask questions about any website using RAG.")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("Website")

    website_url = st.text_input(
        "Enter Website URL",
        placeholder="https://example.com"
    )

    if st.button("Load Website"):

        if website_url.strip() == "":
            st.error("Please enter a website URL.")

        else:

            with st.spinner("Loading Website..."):

                response = requests.post(
                    f"{API_URL}/load",
                    json={
                        "url": website_url
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(data["message"])

                    st.session_state.website_loaded = True

                else:

                    st.error(response.json()["detail"])

    st.divider()

    if st.button("Clear Chat"):

        requests.post(f"{API_URL}/reset")

        st.session_state.messages = []

        st.success("Conversation Cleared")

# -----------------------------
# Chat History
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
if prompt := st.chat_input("Ask your question..."):

    if not st.session_state.website_loaded:

        st.warning("Please load a website first.")

    else:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = requests.post(

                    f"{API_URL}/chat",

                    json={
                        "question": prompt
                    }

                )

                if response.status_code == 200:

                    answer = response.json()["answer"]

                else:

                    answer = "Error generating response."

                st.markdown(answer)

        st.session_state.messages.append(

            {
                "role": "assistant",
                "content": answer
            }

        )