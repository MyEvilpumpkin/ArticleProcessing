from .genre_definition import execute as define_genre
from .summarization import execute as summarize
from .sensitive_topics_definition import execute as define_sensitive_topic

functions = {
    "define_genre": define_genre,
    "summarize": summarize,
    "define_sensitive_topic": define_sensitive_topic
}
