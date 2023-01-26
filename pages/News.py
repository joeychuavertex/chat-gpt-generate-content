import openai
import streamlit as st
from newspaper import Article
import nltk
import pandas as pd
from GoogleNews import GoogleNews
import spacy

nltk.download('punkt')

# Use your OpenAI API key to access GPT-3
openai.api_key = st.secrets["api_key"]


# Use streamlit to create a text input for the user's query
query = st.text_input("Enter your news query:")

# Send the query to GPT-3
search_terms_model = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Find top 20 related search terms for news based on keyword: {query}",
    max_tokens=1024,
    n=5,
    stop=None,
    temperature=0.7,
)


# Use streamlit to display the related search terms
st.write("Related search terms:")
related_result = search_terms_model.choices[0].text.split("\n")[2:]
new_related_result = set()
for item in related_result:
    new_item = item.strip("1234567890. ")
    new_related_result.add(new_item)
st.write(new_related_result)

# use the search terms to query for related news
new_related_list = list(new_related_result)
gn = GoogleNews()
gn.search(
    " OR ".join(new_related_list),
)
news_result = gn.result(sort=True)

nlp = spacy.load('en_core_web_sm')

for article in news_result[:20]:
    article_link = article["link"]
    if article_link:
        try:
            # Article details
            article = Article(article_link)
            article.download()
            article.parse()
            article.nlp()
            article_title = article.title
            article_publish_date = article.publish_date
            article_text = article.text
            article_summary = article.summary
            article_image = article.top_image
            st.markdown(f'[{article_title}]({article_link})')
            st.write(article_publish_date)
            if article_image:
                st.image(article_image)
            st.markdown(f"**Provided summary:** {article_summary}")

            news_model = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{article_text} \n\nTl;dr",
                temperature=0.7,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=1
            )
            news_result = news_model.choices[0]['text']
            st.markdown(f"**GPT-3 summary:** {news_result}")

            # Classification
            shortened_article_text = article.summary[0:200]
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"The following is the categories it falls into: {shortened_article_text} Category: \n\n",
                temperature=0,
                max_tokens=4000,
                top_p=1,
                frequency_penalty=1,
                presence_penalty=1
            )
            classification_result = response.choices[0]["text"]
            st.markdown(f"**News Category:** {classification_result}")

            # NER
            doc = nlp(article_text)
            ents = [(e.text, e.label_) for e in doc.ents]
            df = pd.DataFrame(ents, columns=["Entity", "Label"])
            df = df.drop_duplicates()
            df = df.loc[df['Label'].isin(['PERSON', 'ORG', 'PRODUCT'])]
            st.markdown("**Extract Person, Organization and Product**")
            st.write(df)



        except:
            article_text = "Unable to extract article text."
    else:
        article_text = "Unable to extract article text."