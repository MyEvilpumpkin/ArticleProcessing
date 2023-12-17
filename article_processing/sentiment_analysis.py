from libs.pipeline_loader import pipeline

classifier = pipeline("sentiment-analysis","blanchefort/rubert-base-cased-sentiment")

def execute(text: str) -> str:
    classification_result = classifier(text)[0]["label"]
    sentiment = 'Тональность текста: ' + classification_result
    if classification_result == 'NEUTRAL':
        return sentiment.replace('NEUTRAL','нейтральная')
    elif classification_result == 'POSITIVE':
        return sentiment.replace('POSITIVE','положительная')
    elif classification_result == 'NEGATIVE':
        return sentiment.replace('NEGATIVE','негативная')


