
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
from dotenv import load_dotenv
from groq import Groq
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.extract_comment import extract_video_id,get_comments
from src.llm import analyze_sentiment

st.title("🎬 YouTube Comment Sentiment Analyzer")

yt_url = st.text_input("Enter YouTube Video URL")
if yt_url:
    video_id = extract_video_id(yt_url)

    if not video_id:
        st.error("Invalid YouTube URL. Please check the format.")
    else:
        if st.button("Fetch & Analyze Comments"):
            with st.spinner("Fetching comments..."):
                comments = get_comments(video_id, max_comments=200)

            if comments:
                df = pd.DataFrame(comments, columns=['Comment'])
                with st.spinner("Analyzing sentiments..."):
                    df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

                st.success("Analysis complete!")
                #Sst.write("### Comments with Sentiments(display 5 comments)", df.head())

             
                csv_path = 'youtube_comments_with_sentiment.csv'
                df.to_csv(csv_path, index=False)
                os.remove(csv_path)

                
                st.write("### Sentiment Distribution")
                sentiment_counts = df['Sentiment'].value_counts()
                fig, ax = plt.subplots(figsize=(5, 4))
                ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')
                st.pyplot(fig)

               
                st.download_button(
                    label="📥 Download CSV with Sentiments",
                    data=df.to_csv(index=False),
                    file_name="analyzed_youtube_comments.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No comments found or API error.")