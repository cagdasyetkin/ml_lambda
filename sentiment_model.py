from transformers import pipeline


class SentimentModel:
    def __init__(self):
        self._sentiment_analysis = pipeline("sentiment-analysis",model="ProsusAI/finbert")

    def predict(self, text):
        return self._sentiment_analysis(text)[0]["label"]