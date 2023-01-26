import streamlit as st


def openai_api_key():
    api_key = st.secrets("api_key")
    return api_key


st.title("Communications with GPT-3")
