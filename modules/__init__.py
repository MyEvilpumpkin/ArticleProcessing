from .genre_definition import execute as define_genre
from .language_detection import execute as detect_language
from .summarization import execute as summarize
from .translation import execute as translate
from .sentiment_analysis import execute as analyze_sentiment

modules = {
    "genre_definition": {
        "function": define_genre,
        "title": "Определение жанра",
        "result_title": "Жанр"
    },
    "language_detection": {
        "function": detect_language,
        "title": "Определение языка",
        "result_title": "Язык"
    },
    "summarization": {
        "function": summarize,
        "title": "Краткий пересказ",
        "result_title": "Содержание"
    },
    "translation": {
        "function": translate,
        "title": "Перевод",
        "result_title": "Результат перевода"
    },
    "sentiment_analysis": {
        "function": analyze_sentiment,
        "title": "Анализ тональности",
        "result_title": "Тональность"
    }
}

modules_without_functions = {}
for module_name, module in modules.items():
    modules_without_functions[module_name] = module.copy()
    del modules_without_functions[module_name]["function"]
