from article_processing import analyze_sentiment
from libs.file_reader import read_file
from . import *


def execute_test(file_path):
    expected_sentiment, article_text = read_file(file_path)
    sentiment = analyze_sentiment(article_text)
    assert sentiment == expected_sentiment, f'Expected {expected_sentiment}, but got {sentiment}'


def test_positive_1():
    execute_test(positive_1)


def test_negative_1():
    execute_test(negative_1)


def test_neutral_2():
    execute_test(neutral_1)
