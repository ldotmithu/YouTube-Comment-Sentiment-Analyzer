import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
from dotenv import load_dotenv
from groq import Groq
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
client = Groq(api_key=GROQ_API_KEY)
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def analyze_sentiment(comment):
    prompt = f"""
    Classify the following comment as Positive, Negative, or Neutral:\n
    Comment: "{comment}"\n
    Respond with just one word: Positive, Negative, or Neutral.
    """
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": prompt}]
        )
        raw_sentiment = response.choices[0].message.content.strip()
        cleaned = re.sub(r'[^\w\s]', '', raw_sentiment).capitalize()
        return cleaned if cleaned in ["Positive", "Negative", "Neutral"] else "Neutral"
    except Exception as e:
        st.warning(f"Sentiment analysis error: {e}")
        return "Neutral"
