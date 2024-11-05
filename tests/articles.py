import os

_test_articles_dir = os.path.join('tests', 'articles')


def _get_article_path(article_name: str) -> str:
    return os.path.join(_test_articles_dir, article_name)


all_articles = list()

health_1 = _get_article_path('здоровье_1.txt')
health_2 = _get_article_path('здоровье_2.txt')
science_1 = _get_article_path('наука_1.txt')
science_2 = _get_article_path('наука_2.txt')
politic_1 = _get_article_path('политика_1.txt')
politic_2 = _get_article_path('политика_2.txt')
sport_1 = _get_article_path('спорт_1.txt')
sport_2 = _get_article_path('спорт_2.txt')
economic_1 = _get_article_path('экономика_1.txt')
economic_2 = _get_article_path('экономика_2.txt')

genre_definition_articles = [
    health_1,
    health_2,
    science_1,
    science_2,
    politic_1,
    politic_2,
    sport_1,
    sport_2,
    economic_1,
    economic_2
]

all_articles.extend(genre_definition_articles)

positive_1 = _get_article_path('позитивная_1.txt')
negative_1 = _get_article_path('негативная_1.txt')
neutral_1 = _get_article_path('нейтральная_1.txt')

sentiment_analysis_articles = [
    positive_1,
    negative_1,
    neutral_1
]

all_articles.extend(sentiment_analysis_articles)

ru_1 = _get_article_path('ru_1.txt')
en_1 = _get_article_path('en_1.txt')
de_1 = _get_article_path('de_1.txt')
fr_1 = _get_article_path('fr_1.txt')
it_1 = _get_article_path('it_1.txt')

language_detection_articles = [
    ru_1,
    en_1,
    de_1,
    fr_1,
    it_1
]

all_articles.extend(language_detection_articles)
