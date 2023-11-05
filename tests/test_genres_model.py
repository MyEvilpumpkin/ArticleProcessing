from article_processing import define_genre


def read_file(file_path):
    file_name = file_path.split('/')[-1].split('_')[0]
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_name.lower(), file_content

def test_genres_model_executor(file_path):
    file_name, article_text = read_file(file_path)
    result_defenition_of_article = define_genre(article_text)
    assert (
        file_name == result_defenition_of_article.lower()
    ), ( 
        f"There was no match between the genre and the name in file {file_path}"
    )

def test_health_first_topic():
    file_path = 'test_articles/здоровье_1.txt'
    test_genres_model_executor(file_path)

def test_health_second_topic():
    file_path = 'test_articles/здоровье_2.txt'
    test_genres_model_executor(file_path)

def test_science_first_topic():
    file_path = 'test_articles/наука_1.txt'
    test_genres_model_executor(file_path)

def test_science_second_topic():
    file_path = 'test_articles/наука_2.txt'
    test_genres_model_executor(file_path)

def test_politic_first_topic():
    file_path = 'test_articles/политика_1.txt'
    test_genres_model_executor(file_path)

def test_politic_second_topic():
    file_path = 'test_articles/политика_2.txt'
    test_genres_model_executor(file_path)

def test_sport_first_topic():
    file_path = 'test_articles/спорт_1.txt'
    test_genres_model_executor(file_path)

def test_sport_second_topic():
    file_path = 'test_articles/спорт_2.txt'
    test_genres_model_executor(file_path)

def test_economic_first_topic():
    file_path = 'test_articles/экономика_1.txt'
    test_genres_model_executor(file_path)

def test_economic_second_topic():
    file_path = 'test_articles/экономика_2.txt'
    test_genres_model_executor(file_path)
