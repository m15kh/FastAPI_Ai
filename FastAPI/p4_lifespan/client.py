import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Initialize session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            try:
                image = Image.open(BytesIO(message["content"]))
                st.image(image)
            except Exception:
                st.text("Error displaying image")
        else:
            st.text(message["content"])

# Input from user
if prompt := st.chat_input("Write your prompt in this input field"):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call your API
    response = requests.get(
        "http://localhost:8000/generate/image", params={"prompt": prompt}
    )
    response.raise_for_status()

    # Add assistant message to session state
    st.session_state.messages.append({"role": "assistant", "content": response.content})

    # Display assistant message
    with st.chat_message("assistant"):
        st.text("Here is your generated image")
        try:
            image = Image.open(BytesIO(response.content))
            st.image(image)
        except Exception:
            st.text("Error displaying image")
