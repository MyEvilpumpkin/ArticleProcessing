from modules import detect_language
from libs.file_reader import read_file
from test_articles import ru_1, en_1, de_1, fr_1, it_1


def execute_test(file_path):
    expected_language, article_text = read_file(file_path)
    actual_language = detect_language(article_text)
    assert expected_language == actual_language, f'Expected {expected_language}, but got {actual_language}'


def test_ru_1():
    execute_test(ru_1)


def test_en_1():
    execute_test(en_1)


def test_de_1():
    execute_test(de_1)


def test_fr_1():
    execute_test(fr_1)


def test_it_1():
    execute_test(it_1)
