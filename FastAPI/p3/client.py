
import requests
import streamlit as st

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        content = message["content"]
if isinstance(content, bytes):
    st.audio(content)
else:
    st.markdown(content)
prompt = st.chat_input("Write your prompt in this input field")
if prompt:
    response = requests.get(
    f"http://localhost:8000/generate/audio", params={"prompt": prompt}
    )
response.raise_for_status()
with st.chat_message("assistant"):
    st.text("Here is your generated audio")
    st.audio(response.content)