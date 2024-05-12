import sys

import streamlit as st
from streamlit.web import cli as stcli

from modules import modules


@st.cache_resource
def module_titles():
    return dict([(modules[module]["title"], modules[module]) for module in modules])


def main():
    modules_by_titles = module_titles()
    st.title("Article Processing")
    article_text = st.text_area(label="Статья", placeholder="Введите статью...")
    module_title = st.selectbox(label="Модуль", placeholder="Выберите модуль...", options=modules_by_titles, index=None)
    if article_text != "" and module_title is not None:
        module = modules_by_titles[module_title]
        st.write(f"{module['result_title']} — {module['function'](article_text)}")
    else:
        st.write("После ввода статьи и выбора модуля здесь отобразятся результаты ее обработки")


if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
