from modules import define_genre
from libs.file_reader import read_file
from test_articles import (
    health_1, health_2, science_1, science_2, politic_1, politic_2, sport_1, sport_2, economic_1, economic_2
)


def execute_test(file_path):
    expected_genre, article_text = read_file(file_path)
    actual_genre = define_genre(article_text).lower()
    assert expected_genre == actual_genre, f'Expected {expected_genre}, but got {actual_genre}'


def test_health_1():
    execute_test(health_1)


def test_health_2():
    execute_test(health_2)


def test_science_1():
    execute_test(science_1)


def test_science_2():
    execute_test(science_2)


def test_politic_1():
    execute_test(politic_1)


def test_politic_2():
    execute_test(politic_2)


def test_sport_1():
    execute_test(sport_1)


def test_sport_2():
    execute_test(sport_2)


def test_economic_1():
    execute_test(economic_1)


def test_economic_2():
    execute_test(economic_2)
