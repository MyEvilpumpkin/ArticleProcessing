import pytest

from modules import analyze_sentiment
from libs.file_reader import read_file
from tests.articles import sentiment_analysis_articles as articles


@pytest.mark.parametrize('article_path', articles)
def test(article_path: str):
    expected_sentiment, article_text = read_file(article_path)
    actual_sentiment = analyze_sentiment(article_text)
    assert expected_sentiment == actual_sentiment, f'Expected {expected_sentiment}, but got {actual_sentiment}'
