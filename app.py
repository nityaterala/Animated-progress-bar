# app.py

import streamlit as st
import pickle
import re
import string
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Spam Detector",
    page_icon="📧",
    layout="centered"
)

# -----------------------------
# DARK CSS STYLE
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
.big-title {
    font-size: 34px;
    font-weight: bold;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #9aa0a6;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    font-size: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -----------------------------
# TEXT CLEANING
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# -----------------------------
# UI HEADER
# -----------------------------
st.markdown('<p class="big-title">📧 AI Spam Message Detector</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Dark Mode • NLP • Machine Learning</p>', unsafe_allow_html=True)

st.write("")

user_input = st.text_area("Enter your message:", height=150)

# -----------------------------
# BUTTON ACTION
# -----------------------------
if st.button("🔍 Analyze Message"):

    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:

        # Animated Progress Bar
        progress = st.progress(0)
        status_text = st.empty()

        for i in range(101):
            progress.progress(i)
            status_text.write(f"🤖 AI analyzing... {i}%")
            time.sleep(0.015)

        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        st.write("")

        if prediction == "spam":
            st.markdown(
                '<div class="result-box" style="background-color:#3a0d11;color:#ff4b4b;">🚨 SPAM MESSAGE DETECTED</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-box" style="background-color:#0f2e1d;color:#00ffae;">✅ SAFE MESSAGE</div>',
                unsafe_allow_html=True
            )
