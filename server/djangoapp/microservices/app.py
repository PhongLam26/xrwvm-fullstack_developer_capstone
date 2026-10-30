from pathlib import Path

import nltk
from flask import Flask, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer

BASE_DIR = Path(__file__).resolve().parent
nltk.data.path.insert(0, str(BASE_DIR))

app = Flask("Sentiment Analyzer")
sia = SentimentIntensityAnalyzer()


@app.get("/")
def home():
    return jsonify(
        {
            "service": "Sentiment Analyzer",
            "usage": "GET /analyze/<text>",
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/analyze/<path:input_text>")
def analyze_sentiment(input_text):
    if not input_text.strip():
        return jsonify({"error": "Text is required."}), 400
    scores = sia.polarity_scores(input_text)
    compound = scores["compound"]
    sentiment = (
        "positive"
        if compound >= 0.05
        else "negative" if compound <= -0.05 else "neutral"
    )
    return jsonify({"sentiment": sentiment, "scores": scores})


@app.errorhandler(LookupError)
def missing_vader_data(_error):
    return jsonify({"error": "The VADER lexicon is unavailable."}), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False)
