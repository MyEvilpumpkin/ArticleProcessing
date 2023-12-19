from article_processing import define_genre
from libs.file_reader import read_file
from . import *


def execute_test(file_path):
    file_name, article_text = read_file(file_path)
    defined_genre = define_genre(article_text)
    assert (
        file_name == defined_genre.lower()
    ), ( 
        f'There was no match between the genre and the name in file {file_path}'
    )


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

