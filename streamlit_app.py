import sys

import streamlit as st
from streamlit.web import cli as stcli

from article_processing import define_genre, summarize


def main():
    st.title("Article Processing")
    article = st.text_area("Статья", placeholder="Введите статью...")
    if article != "":
        st.write(f"Жанр — {define_genre(article)}")
        st.write(f"Содержание — {summarize(article)}")
        st.write("Обработка статьи завершена!")
    else:
        st.write("После ввода статьи здесь отобразятся результаты ее обработки")


if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
