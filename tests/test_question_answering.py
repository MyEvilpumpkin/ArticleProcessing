from fastapi.testclient import TestClient

from tests.test_web_app import execute_genre_definition_test
from web_app import app
from article_processing import modules_without_functions
from libs.file_reader import read_file

client = TestClient(app)

def execute_us_test(file_path: str):
    text = read_file(file_path)
    question = 'о чем текст?'
    response = client.post(
        "/api/module/question_answering",
        json={"text": text, "question": question}
    )
    assert response.status_code == 200
    assert isinstance(response.text, str)


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
