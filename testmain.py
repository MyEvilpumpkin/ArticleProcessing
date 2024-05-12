import unittest
from unittest.mock import patch
from streamlit_answer_question import main

class TestMainFunction(unittest.TestCase):
    @patch('streamlit.write')
    def test_main(self, mock_write):
        # Подготовка
        mock_write.side_effect = lambda x: None  # Мокаем streamlit.write, чтобы не выводить на экран

        # Вызов функции main
        main()

        # Проверка, что функция main вызывает streamlit.write с ожидаемыми аргументами
        mock_write.assert_any_call("Article Processing")
        mock_write.assert_any_call("Статья")
        mock_write.assert_any_call("Вопрос")
        mock_write.assert_any_call("Обработка статьи завершена!")

if __name__ == '__main__':
    unittest.main()
