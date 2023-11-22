from article_processing import detection_language


def read_file(file_path):
    file_name = file_path.split('/')[-1].split('_')[0]
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()
    return file_name.lower(), file_content


def execute_lang_detect_test(file_path):
    file_name, article_text = read_file(file_path)
    detect_lang_title = detection_language(file_name)
    detect_lang_text = detection_language(article_text)
    assert detect_lang_title == 'ru', f"Title language check failed in file {file_path}"
    assert detect_lang_text == 'ru', f"Text language check failed in file {file_path}"


def test_health_first_topic():
    file_path = 'test_articles/здоровье_1.txt'
    execute_lang_detect_test(file_path)


def test_health_second_topic():
    file_path = 'test_articles/здоровье_2.txt'
    execute_lang_detect_test(file_path)


# def test_science_first_topic():
#     file_path = 'test_articles/наука_1.txt'
#     execute_lang_detect_test(file_path)


# def test_science_second_topic():
#     file_path = 'test_articles/наука_2.txt'
#     execute_lang_detect_test(file_path)


# def test_politic_first_topic():
#     file_path = 'test_articles/политика_1.txt'
#     execute_lang_detect_test(file_path)


# def test_politic_second_topic():
#     file_path = 'test_articles/политика_2.txt'
#     execute_lang_detect_test(file_path)


# def test_sport_first_topic():
#     file_path = 'test_articles/спорт_1.txt'
#     execute_lang_detect_test(file_path)


# def test_sport_second_topic():
#     file_path = 'test_articles/спорт_2.txt'
#     execute_lang_detect_test(file_path)


def test_economic_first_topic():
    file_path = 'test_articles/экономика_1.txt'
    execute_lang_detect_test(file_path)


def test_economic_second_topic():
    file_path = 'test_articles/экономика_2.txt'
    execute_lang_detect_test(file_path)
