from libs.pipeline_loader import pipeline

classifier = pipeline('sentiment-analysis', 'blanchefort/rubert-base-cased-sentiment')


def execute(text: str) -> str:
    sentiment = classifier(text)[0]['label']

    if sentiment == 'POSITIVE':
        return 'позитивная'
    elif sentiment == 'NEGATIVE':
        return 'негативная'
    elif sentiment == 'NEUTRAL':
        return 'нейтральная'
