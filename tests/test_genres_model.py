from article_processing import define_genre
import os
import unittest


def read_file(file_path):
    file_name = file_path.split('/')[1].split('_')[0]
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents, file_name


class Test(unittest.TestCase):
    def test_health_first_topic(self):
        file_path = 'test_articles/здоровье_1.txt'
        health_first_file_name, health_first_article_text = read_file(file_path)
        result_defenition_of_health_first_article = define_genre(health_first_article_text)
        self.assertEqual(
            health_first_file_name,
            result_defenition_of_health_first_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_health_second_topic(self):
        file_path = 'test_articles/здоровье_2.txt'
        health_second_file_name, health_second_article_text = read_file(file_path)
        result_defenition_of_health_second_article = define_genre(health_second_article_text)
        self.assertEqual(
            health_second_file_name,
            result_defenition_of_health_second_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_science_first_topic(self):
        file_path = 'test_articles/наука_1.txt'
        science_first_file_name, science_first_article_text = read_file(file_path)
        result_defenition_of_science_first_article = define_genre(science_first_article_text)
        self.assertEqual(
            science_first_file_name,
            result_defenition_of_science_first_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_science_second_topic(self):
        file_path = 'test_articles/наука_2.txt'
        science_second_file_name, science_second_article_text = read_file(file_path)
        result_defenition_of_science_second_article = define_genre(science_second_article_text)
        self.assertEqual(
            science_second_file_name,
            result_defenition_of_science_second_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_politic_first_topic(self):
        file_path = 'test_articles/политика_1.txt'
        politic_first_file_name, politic_first_article_text = read_file(file_path)
        result_defenition_of_politic_first_article = define_genre(politic_first_article_text)
        self.assertEqual(
            politic_first_file_name,
            result_defenition_of_politic_first_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_politic_second_topic(self):
        file_path = 'test_articles/политика_2.txt'
        politic_second_file_name, politic_second_article_text = read_file(file_path)
        result_defenition_of_politic_second_article = define_genre(politic_second_article_text)
        self.assertEqual(
            politic_second_file_name,
            result_defenition_of_politic_second_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_sport_first_topic(self):
        file_path = 'test_articles/cпорт_1.txt'
        sport_first_file_name, sport_first_article_text = read_file(file_path)
        result_defenition_of_sport_first_article = define_genre(sport_first_article_text)
        self.assertEqual(
            sport_first_file_name,
            result_defenition_of_sport_first_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_sport_second_topic(self):
        file_path = 'test_articles/cпорт_2.txt'
        sport_second_file_name, sport_second_article_text = read_file(file_path)
        result_defenition_of_sport_second_article = define_genre(sport_second_article_text)
        self.assertEqual(
            sport_second_file_name,
            result_defenition_of_sport_second_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_economic_first_topic(self):
        file_path = 'test_articles/экономика_1.txt'
        economic_first_file_name, economic_first_article_text = read_file(file_path)
        result_defenition_of_economic_firtst_article = define_genre(economic_first_article_text)
        self.assertEqual(
            economic_first_file_name,
            result_defenition_of_economic_firtst_article,
            f"There was no match between the genre and the name in file {file_path}"
        )

    def test_economic_second_topic(self):
        file_path = 'test_articles/экономика_2.txt'
        economic_second_file_name, economic_second_article_text = read_file(file_path)
        result_defenition_of_economic_second_article = define_genre(economic_second_article_text)
        self.assertEqual(
            economic_second_file_name,
            result_defenition_of_economic_second_article,
            f"There was no match between the genre and the name in file {file_path}"
        )
