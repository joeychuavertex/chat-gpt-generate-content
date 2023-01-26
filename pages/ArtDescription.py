import openai
import streamlit as st

openai.api_key = st.secrets["api_key"]

st.title("Art Description Generator")
input = st.text_input("Generate description based on:", placeholder="Describe in detail the center of a village during christmas")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Generate detailed description on {input}",
  temperature=0.3,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


st.write(response.choices[0]['text'])


kwargs = {
             "engine": "text-davinci-003",
             "temperature": 0.85,
             "max_tokens": 600,
             "best_of": 1,
             "top_p": 1,
             "frequency_penalty": 0,
             "presence_penalty": 0,
             "stop": ["###"],
         }