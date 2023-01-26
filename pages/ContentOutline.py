import streamlit as st
from model_content_outline import GeneralModel

def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    # api_key = st.sidebar.text_input("APIkey", type="password")
    api_key = st.secrets("api_key")

    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Generate content outline based on:")

        # st.write("---")

        s_example = "Venture Capital"
        input = st.text_area(
            "Use the example below or input your own text in English",
            value=s_example,
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")

st.set_page_config(page_title="GPT-3 for Comms", page_icon=":shark:", layout="wide")

app()