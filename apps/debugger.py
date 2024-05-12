from libs.file_reader import read_file

from modules import detect_language as module
from test_articles import science_1 as article_file_path

if __name__ == "__main__":
    _, article_text = read_file(article_file_path)
    print(module(article_text))
