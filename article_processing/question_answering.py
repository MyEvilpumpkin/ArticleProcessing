from libs.pipeline_loader import pipeline

qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")


def execute(text: str, question: str = "") -> str:
    answer = qa_model(question=question, context=text)
    return answer["answer"]
