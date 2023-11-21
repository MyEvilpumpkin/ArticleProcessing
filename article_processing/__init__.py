from .genre_definition import execute as define_genre
from .language_detection import execute as detection_language
from .summarization import execute as summarize

modules = {
    "genre_definition": {
        "function": define_genre,
        "title": "Определение жанра",
        "result_title": "Жанр"
    },
    "language_classification": {
        "function": detection_language,
        "title": "Определение языка",
        "result_title": "Язык"
    },
    "summarization": {
        "function": summarize,
        "title": "Краткий пересказ",
        "result_title": "Содержание"
    }
}
