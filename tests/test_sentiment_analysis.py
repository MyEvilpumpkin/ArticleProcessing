from modules import analyze_sentiment
from libs.file_reader import read_file
from tests.articles import positive_1, negative_1, neutral_1


def execute_test(file_path):
    expected_sentiment, article_text = read_file(file_path)
    actual_sentiment = analyze_sentiment(article_text)
    assert expected_sentiment == actual_sentiment, f'Expected {expected_sentiment}, but got {actual_sentiment}'


def test_positive_1():
    execute_test(positive_1)


def test_negative_1():
    execute_test(negative_1)


def test_neutral_2():
    execute_test(neutral_1)
