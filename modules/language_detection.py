from libs.pipeline_loader import pipeline

classifier = pipeline("text-classification", "papluca/xlm-roberta-base-language-detection")


def execute(text: str) -> str:
    classification_result = classifier(text)
    return classification_result[0]["label"]
