import os
from urllib.parse import quote

import requests

BACKEND_URL = os.getenv(
    "BACKEND_URL", os.getenv("backend_url", "http://127.0.0.1:3030")
).rstrip("/")
SENTIMENT_ANALYZER_URL = os.getenv(
    "SENTIMENT_ANALYZER_URL",
    os.getenv("sentiment_analyzer_url", "http://127.0.0.1:5050"),
).rstrip("/")
REQUEST_TIMEOUT = float(os.getenv("SERVICE_REQUEST_TIMEOUT", "5"))


def get_request(endpoint):
    response = requests.get(
        f"{BACKEND_URL}/{endpoint.lstrip('/')}", timeout=REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()


def analyze_review_sentiments(text):
    response = requests.get(
        f"{SENTIMENT_ANALYZER_URL}/analyze/{quote(text, safe='')}",
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    result = response.json()
    if result.get("sentiment") not in {"positive", "neutral", "negative"}:
        raise ValueError("Sentiment service returned an invalid classification.")
    return result


def post_review(data_dict):
    response = requests.post(
        f"{BACKEND_URL}/insert_review",
        json=data_dict,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()
