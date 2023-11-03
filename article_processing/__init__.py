from .genre_definition import execute as define_genre
from .summarization import execute as summarize

functions = {
    "define_genre": define_genre,
    "summarize": summarize
}
