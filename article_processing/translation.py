from libs.pipeline_loader import pipeline

translator = pipeline('translation', model='Helsinki-NLP/opus-mt-ru-en')


def execute(text: str) -> str:
    translation_result = translator(text)
    return translation_result[0]['translation_text']
