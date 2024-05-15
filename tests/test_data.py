import re

import pytest

from libs.file_reader import read_file
from tests.articles import all_articles as articles
from tests.articles import language_detection_articles as lang_articles


def len_test(article_text: str):
    metric = len(article_text)
    assert metric > 100, f'Len metric: Expected > {100}, but got {metric}'


def lang_test(article_path: str, article_text: str):
    is_ru_article = article_path not in lang_articles or 'ru' in article_path
    ru_chars = re.findall('[А-Яа-яЁё]', article_text)
    en_chars = re.findall('[a-zA-Z]', article_text)
    metric = len(ru_chars if is_ru_article else en_chars) / len(article_text)
    assert metric > 0.70, f'Lang metric: Expected > {0.70}, but got {metric:.2f}'


@pytest.mark.parametrize('article_path', articles)
def test(article_path: str):
    _, article_text = read_file(article_path)
    len_test(article_text)
    lang_test(article_path, article_text)
