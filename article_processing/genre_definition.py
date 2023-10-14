from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
genres = ["спорт", "политика", "экономика", "здоровье", "наука"]


def execute(text: str) -> str:
    classification_result = classifier(text, genres, multi_label=False)
    return classification_result["labels"][0].capitalize()
