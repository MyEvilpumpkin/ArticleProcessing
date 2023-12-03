import sys

import streamlit as st
from streamlit.web import cli as stcli

from article_processing import modules


def main():
    st.title("Article Processing")
    article_text = st.text_area("Статья", placeholder="Введите статью...")
    article_question = st.text_area("Вопрос", placeholder="Введите вопрос...")
    if article_text != "" and article_question != "":
        module_name = "question_answering"
        module = modules[module_name]
        st.write(f"{module['result_title']} — {module['function'](article_text, article_question)}")
        st.write("Обработка статьи завершена!")
    else:
        st.write("После ввода статьи здесь отобразятся результаты ее обработки")


if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
