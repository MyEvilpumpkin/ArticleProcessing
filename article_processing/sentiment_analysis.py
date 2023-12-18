from libs.pipeline_loader import pipeline

classifier = pipeline("sentiment-analysis","blanchefort/rubert-base-cased-sentiment")

def execute(text: str) -> str:
    sentiment = classifier(text)[0]["label"]
    if sentiment == 'NEUTRAL':
        return sentiment.replace('NEUTRAL','нейтральная')
    elif sentiment == 'POSITIVE':
        return sentiment.replace('POSITIVE','положительная')
    elif sentiment == 'NEGATIVE':
        return sentiment.replace('NEGATIVE','негативная')


