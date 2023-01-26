import openai
import streamlit as st

openai.api_key = st.secrets["api_key"]

st.title("Article Content Generator")
input = st.text_input("Generate article content based on:", placeholder="Venture Capital")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Generate detailed article based on the topic of {input}",
  temperature=0.3,
  max_tokens=4000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


st.write(response.choices[0]['text'])