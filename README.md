# 🎬 YouTube Comment Sentiment Analyzer

This is a Streamlit-based web application that analyzes sentiments (Positive, Negative, or Neutral) of comments from a YouTube video using a powerful LLM model hosted via the Groq API.

---

## 🚀 Features

- 🔗 Input any YouTube video URL
- 💬 Extract up to 200 top-level comments
- 🧠 Use Groq LLM (`llama-4-scout`) to analyze comment sentiment
- 📊 Visualize sentiment distribution using a pie chart
- 📥 Download analyzed results as a CSV file

---

## 📦 Technologies Used

- [Streamlit](https://streamlit.io/) – Web app framework
- [Groq API](https://console.groq.com/) – Access to fast LLMs (e.g., LLaMA-4)
- [YouTube Data API v3](https://developers.google.com/youtube/v3) – For fetching video comments
- `pandas`, `matplotlib`, `re` – For data processing and visualization
- `dotenv` – Secure API key loading

---

## 🧪 Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/ldotmithu/YouTube-Comment-Sentiment-Analyzer.git
cd YouTube-Comment-Sentiment-Analyzer
```

2. **Run the Application:**
```bash
streamlit run app.py
```
#### Then open your browser to http://localhost:8501.

3. **Set Environment Variables:**
```.env
GROQ_API_KEY=your_groq_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

## 🛡️ Disclaimer

This app uses AI models and may not always return perfect results. It is meant for educational or exploratory purposes only.

---
### Contributor: L. Mithurshan
---

### License 📝
This project is licensed under the Apache License 📜
---

## **Glance of the Project**

![image](https://github.com/ldotmithu/Dataset/blob/main/Screenshot%20(12).png)
![image](https://github.com/ldotmithu/Dataset/blob/main/Screenshot%20(13).png)
---

Happy coding! 😊
