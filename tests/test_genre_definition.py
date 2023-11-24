from article_processing import define_genre
from libs.file_reader import read_file


def execute_genre_definition_test(file_path):
    file_name, article_text = read_file(file_path)
    defined_genre = define_genre(article_text)
    assert (
        file_name == defined_genre.lower()
    ), ( 
        f'There was no match between the genre and the name in file {file_path}'
    )


def test_health_1():
    file_path = 'test_articles/здоровье_1.txt'
    execute_genre_definition_test(file_path)


def test_health_2():
    file_path = 'test_articles/здоровье_2.txt'
    execute_genre_definition_test(file_path)


def test_science_1():
    file_path = 'test_articles/наука_1.txt'
    execute_genre_definition_test(file_path)


def test_science_2():
    file_path = 'test_articles/наука_2.txt'
    execute_genre_definition_test(file_path)


def test_politic_1():
    file_path = 'test_articles/политика_1.txt'
    execute_genre_definition_test(file_path)


def test_politic_2():
    file_path = 'test_articles/политика_2.txt'
    execute_genre_definition_test(file_path)


def test_sport_1():
    file_path = 'test_articles/спорт_1.txt'
    execute_genre_definition_test(file_path)


def test_sport_2():
    file_path = 'test_articles/спорт_2.txt'
    execute_genre_definition_test(file_path)


def test_economic_1():
    file_path = 'test_articles/экономика_1.txt'
    execute_genre_definition_test(file_path)


def test_economic_2():
    file_path = 'test_articles/экономика_2.txt'
    execute_genre_definition_test(file_path)
