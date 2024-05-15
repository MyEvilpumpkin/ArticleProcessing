import pytest
from fastapi.testclient import TestClient

from apps.api_app import app
from modules import modules_without_functions
from libs.file_reader import read_file
from tests.articles import genre_definition_articles as articles

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


@pytest.mark.parametrize('file_path', articles)
def test_genre_definition(file_path: str):
    module_name = 'genre_definition'
    genre, text = read_file(file_path)
    response = get_module_response(module_name, text)
    assert response.status_code == 200
    assert response.json() == {
        'module_name': module_name,
        'result': genre
    }
