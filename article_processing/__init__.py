from .genre_definition import execute as define_genre
from .summarization import execute as summarize

modules = {
    "genre_definition": {
        "function": define_genre,
        "title": "Определение жанра",
        "result_title": "Жанр"
    },
    "summarization": {
        "function": summarize,
        "title": "Краткий пересказ",
        "result_title": "Содержание"
    }
}
