import streamlit as st
import requests
from utils import get_news_articles, analyze_sentiment, generate_tts

st.title("News Sentiment & TTS App")

company = st.text_input("Enter a company name")
if st.button("Analyze"):
    news = get_news_articles(company)
    
    st.subheader("News Articles")
    for article in news:
        sentiment = analyze_sentiment(article["title"])
        st.write(f"**{article['title']}** ({sentiment})")
        st.write(f"[Read more]({article['link']})")

    st.subheader("Generating Hindi Speech...")
    summary_text = f"{company} के समाचार का विश्लेषण किया गया है।"
    audio_path = generate_tts(summary_text)

    st.audio(audio_path)
