import os

_test_articles_dir = 'test_articles'


def _get_article_path(article_name: str) -> str:
    return os.path.join(_test_articles_dir, article_name)


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

positive_1 = _get_article_path('позитивная_1.txt')
negative_1 = _get_article_path('негативная_1.txt')
neutral_1 = _get_article_path('нейтральная_1.txt')

ru_1 = _get_article_path('ru_1.txt')
en_1 = _get_article_path('en_1.txt')
de_1 = _get_article_path('de_1.txt')
fr_1 = _get_article_path('fr_1.txt')
it_1 = _get_article_path('it_1.txt')
