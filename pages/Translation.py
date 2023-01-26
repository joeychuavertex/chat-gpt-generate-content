import openai
import streamlit as st

openai.api_key = st.secrets["api_key"]

st.title("Translation")
input = st.text_input("Enter text for translation into Chinese, Japanese, Korean")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Translate {input} into 1. Chinese 2. Japanese 3. Korean:",
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


st.write(response.choices[0]['text'])