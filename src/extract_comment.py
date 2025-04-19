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

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:\S+)?", url)
    return match.group(1) if match else None


def get_comments(video_id, max_comments=100):
    comments = []
    next_page_token = None

    try:
        while len(comments) < max_comments:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=min(100, max_comments - len(comments)),
                pageToken=next_page_token,
                textFormat="plainText"
            )
            response = request.execute()

            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
    except HttpError as e:
        st.error(f"Failed to fetch comments: {e}")
        return []

    return comments
