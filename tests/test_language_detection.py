import pytest

from modules import detect_language
from libs.file_reader import read_file
from tests.articles import language_detection_articles as articles


@pytest.mark.parametrize('article_path', articles)
def test(article_path: str):
    expected_language, article_text = read_file(article_path)
    actual_language = detect_language(article_text)
    assert expected_language == actual_language, f'Expected {expected_language}, but got {actual_language}'
