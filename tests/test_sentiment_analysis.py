import pytest

from modules import analyze_sentiment
from libs.file_reader import read_file
from tests.articles import sentiment_analysis_articles as articles


@pytest.mark.parametrize('file_path', articles)
def test(file_path):
    expected_sentiment, article_text = read_file(file_path)
    actual_sentiment = analyze_sentiment(article_text)
    assert expected_sentiment == actual_sentiment, f'Expected {expected_sentiment}, but got {actual_sentiment}'
