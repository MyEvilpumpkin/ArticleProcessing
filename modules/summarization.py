from libs.pipeline_loader import pipeline

summarizer = pipeline('summarization', model='d0rj/rut5-base-summ')


def execute(text: str) -> str:
    summarization_result = summarizer(text)
    return summarization_result[0]['summary_text']
