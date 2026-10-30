FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
COPY sentiment ./sentiment

ENV NLTK_DATA=/app/sentiment
EXPOSE 5050
CMD ["python", "app.py"]
