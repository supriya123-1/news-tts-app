import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from keybert import KeyBERT
from TTS.api import TTS

# Function to get news articles
def get_news_articles(company_name):
    search_url = f"https://news.google.com/rss/search?q={company_name}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "xml")
    
    articles = []
    for item in soup.find_all("item")[:10]:  # Get top 10 articles
        title = item.title.text
        link = item.link.text
        pub_date = item.pubDate.text
        articles.append({"title": title, "link": link, "date": pub_date})
    
    return articles

# Function for sentiment analysis
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)["compound"]
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Function for keyword extraction
def extract_keywords(text):
    kw_model = KeyBERT()
    return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2))

# Function to generate Hindi TTS audio
def generate_tts(text, output_file="output/speech.mp3"):
    tts = TTS(model_name="coqui-ai/tts-hi")
    tts.tts_to_file(text=text, file_path=output_file)
    return output_file
