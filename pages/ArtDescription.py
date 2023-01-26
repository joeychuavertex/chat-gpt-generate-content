import openai
import streamlit as st

openai.api_key = st.secrets["api_key"]

st.title("Content")
input = st.text_input("Generate description based on:", placeholder="Describe in detail the center of a village during christmas")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Generate detailed description on {input}",
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


st.write(response.choices[0]['text'])