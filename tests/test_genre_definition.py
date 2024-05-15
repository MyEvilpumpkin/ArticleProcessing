import pytest

from modules import define_genre
from libs.file_reader import read_file
from tests.articles import genre_definition_articles as articles


@pytest.mark.parametrize('article_path', articles)
def test(article_path: str):
    expected_genre, article_text = read_file(article_path)
    actual_genre = define_genre(article_text).lower()
    assert expected_genre == actual_genre, f'Expected {expected_genre}, but got {actual_genre}'
