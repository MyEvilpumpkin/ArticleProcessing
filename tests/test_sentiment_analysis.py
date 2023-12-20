from article_processing import analyze_sentiment
from libs.file_reader import read_file


def execute_test(file_path, expected_sentiment):
    _, article_text = read_file(file_path)
    sentiment = analyze_sentiment(article_text)
    assert sentiment == expected_sentiment, f'Expected {expected_sentiment}, but got {sentiment}'


def test_positive_sentiment():
    execute_test('test_articles/положительная_1.txt', 'положительная')


def test_negative_sentiment():
    execute_test('test_articles/негативная_1.txt', 'негативная')


def test_neutral_sentiment():
    execute_test('test_articles/нейтральная_1.txt', 'нейтральная')
