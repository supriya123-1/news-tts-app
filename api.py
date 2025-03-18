from fastapi import FastAPI
from utils import get_news_articles, analyze_sentiment, generate_tts

app = FastAPI()

@app.get("/news/{company}")
def get_news(company: str):
    return get_news_articles(company)

@app.get("/sentiment/{text}")
def get_sentiment(text: str):
    return {"sentiment": analyze_sentiment(text)}

@app.post("/tts/")
def generate_speech(text: str):
    file_path = generate_tts(text)
    return {"audio_file": file_path}
