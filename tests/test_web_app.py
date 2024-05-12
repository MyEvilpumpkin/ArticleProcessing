from fastapi.testclient import TestClient

from web_app import app
from modules import modules_without_functions
from libs.file_reader import read_file
from . import health_1, health_2, science_1, science_2, politic_1, politic_2, sport_1, sport_2, economic_1, economic_2


client = TestClient(app)


def test_modules():
    response = client.get('/api/modules')
    assert response.status_code == 200
    assert response.json() == modules_without_functions


def get_module_response(module_name: str, text: str):
    return client.post(
        f'/api/modules/{module_name}',
        json={'text': text}
    )


def execute_genre_definition_test(file_path: str):
    module_name = 'genre_definition'
    genre, text = read_file(file_path)
    response = get_module_response(module_name, text)
    assert response.status_code == 200
    assert response.json() == {
        'module_name': module_name,
        'result': genre
    }


def test_health_1():
    execute_genre_definition_test(health_1)


def test_health_2():
    execute_genre_definition_test(health_2)


def test_science_1():
    execute_genre_definition_test(science_1)


def test_science_2():
    execute_genre_definition_test(science_2)


def test_politic_1():
    execute_genre_definition_test(politic_1)


def test_politic_2():
    execute_genre_definition_test(politic_2)


def test_sport_1():
    execute_genre_definition_test(sport_1)


def test_sport_2():
    execute_genre_definition_test(sport_2)


def test_economic_1():
    execute_genre_definition_test(economic_1)


def test_economic_2():
    execute_genre_definition_test(economic_2)
