import pytest

from libs.file_reader import read_file
from tests.articles import all_articles as articles


def len_test(article_text):
    assert len(article_text) > 100


@pytest.mark.parametrize('file_path', articles)
def test(file_path: str):
    _, article_text = read_file(file_path)
    len_test(article_text)
