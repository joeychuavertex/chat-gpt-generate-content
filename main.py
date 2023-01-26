import streamlit as st

st.title("API Key:")


def openai_api_key():
    api_key = st.secrets("api_key")
    st.text_input(api_key)
    return api_key
