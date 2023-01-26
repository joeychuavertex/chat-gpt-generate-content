import openai
import streamlit as st

openai.api_key = st.secrets["openai_api_key"]

st.title("Translation")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Translate this into 1. Japanese 2. Chinese 3. Korean:",
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


st.write(response.choices[0])