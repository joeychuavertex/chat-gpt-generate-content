import openai
import streamlit as st

openai.api_key = st.secrets["api_key"]

st.title("Social Media Posts")
input = st.text_area("Suggest social media posts:", placeholder="Venture Capital")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Suggest social media posts on {input}",
  temperature=0.3,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


st.write(response.choices[0]['text'])