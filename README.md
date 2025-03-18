# News Summarization & Hindi TTS Application

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd news-tts-app
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   pip install -r requirements.txt
   ```

3. Run the FastAPI backend:
   ```bash
   uvicorn api:app --reload
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Features

- Scrapes latest news about a given company.
- Performs sentiment analysis.
- Generates a comparative analysis report.
- Converts key insights into Hindi speech.
- Provides an easy-to-use web interface.
