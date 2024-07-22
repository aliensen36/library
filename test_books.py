import unittest
import os
import json
from books import Library

class TestLibrary(unittest.TestCase):

    # Создание временного файла библиотеки для тестирования
    def setUp(self):
        self.test_file = 'test_library.json'
        self.library = Library(self.test_file)

    # Удаление временного файла
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # Тестирование добавления книги
    def test_add_book(self):
        self.library.add_book("Test Title", "Test Author", "2024")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Title")

    # Тестирование удаления книги
    def test_remove_book(self):
        self.library.add_book("Test Title", "Test Author", "2024")
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    # Тестирование поиска книги по ID
    def test_find_book_by_id(self):
        self.library.add_book("Test Title", "Test Author", "2024")
        book = self.library.find_book_by_id(1)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Test Title")

    # Тестирование поиска книг по разным критериям
    def test_search_books(self):
        self.library.add_book("Test Title 1", "Test Author", "2024")
        self.library.add_book("Test Title 2", "Test Author", "2023")
        results = self.library.search_books(title="Test Title 1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Title 1")

    # Тестирование изменения статуса книги
    def test_change_status(self):
        self.library.add_book("Test Title", "Test Author", "2024")
        self.library.change_status(1, "выдана")
        book = self.library.find_book_by_id(1)
        self.assertEqual(book.status, "выдана")

    # Тестирование загрузки данных из файла
    def test_load_data(self):
        self.library.add_book("Test Title", "Test Author", "2024")
        self.library.save_data()
        new_library = Library(self.test_file)
        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].title, "Test Title")

    # Тестирование сохранения данных в файл
    def test_save_data(self):
        self.library.add_book("Test Title", "Test Author", "2024")
        self.library.save_data()
        with open(self.test_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "Test Title")

if __name__ == "__main__":
    unittest.main()
