import pytest

from modules import define_genre
from libs.file_reader import read_file
from tests.articles import genre_definition_articles as articles


@pytest.mark.parametrize('file_path', articles)
def test(file_path):
    expected_genre, article_text = read_file(file_path)
    actual_genre = define_genre(article_text).lower()
    assert expected_genre == actual_genre, f'Expected {expected_genre}, but got {actual_genre}'
