from article_processing import define_genre, detection_language, summarize, answer_question
from libs.file_reader import read_file

_, article_text = read_file("test_articles/экономика_2.txt")

if __name__ == "__main__":
    # print(define_genre(article_text))
    # print(detection_language(article_text))
    # print(summarize(article_text))
    print(answer_question(article_text, "Это текст про банки?"))

