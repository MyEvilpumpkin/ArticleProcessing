from fastapi.testclient import TestClient

from web_app import app
from article_processing import modules_without_functions

client = TestClient(app)


def read_file(file_path):
    file_name = file_path.split('/')[-1].split('_')[0]
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_name.lower(), file_content


def test_modules():
    response = client.get('/api/modules')
    assert response.status_code == 200
    assert response.json() == modules_without_functions


def execute_genre_definition_test(file_path: str):
    module_name = 'genre_definition'
    genre, text = read_file(file_path)
    response = client.post(
        f'/api/modules/{module_name}',
        json={'text': text}
    )
    assert response.status_code == 200
    assert response.json() == {
        'module_name': module_name,
        'result': genre
    }


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
