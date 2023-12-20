from article_processing import *
from libs.file_reader import read_file

_, article_text = read_file("test_articles/экономика_2.txt")

if __name__ == "__main__":
    # print(define_genre(article_text))
    # print(detect_language(article_text))
    # print(summarize(article_text))
    # print(translate(article_text))
    print(analyze_sentiment(article_text))
