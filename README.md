# Система управления библиотекой

## Описание

Этот проект реализует простую систему управления библиотекой на языке Python. Она позволяет пользователям управлять книгами в библиотеке: добавлять, удалять, искать, отображать все книги и изменять статус книги.

## Функционал

1. **Добавление книги**: Добавляет новую книгу в библиотеку с названием, автором и годом издания.
2. **Удаление книги**: Удаляет книгу из библиотеки по ее ID.
3. **Поиск книг**: Ищет книги по названию, автору или году издания.
4. **Отображение всех книг**: Показывает все книги, находящиеся в библиотеке.
5. **Изменение статуса книги**: Изменяет статус книги (например, "в наличии" или "выдана").

## Классы

### Класс `Book`

Класс `Book` представляет отдельную книгу в библиотеке.

```python
class Book:
    def __init__(self, id, title, author, year, status="в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
```

### Класс `Library`

Класс `Library` управляет коллекцией объектов `Book`.

```python
class Library:
    def __init__(self, data_file="library.json"):
        self.data_file = data_file
        self.books = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]
        else:
            self.books = []

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_data()
        print(f"Книга '{title}' добавлена с ID {book_id}.")

    def remove_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_data()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key, '').lower() == value.lower()]
        return results

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def change_status(self, book_id, new_status):
        book = self.find_book_by_id(book_id)
        if book:
            book.status = new_status
            self.save_data()
            print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
```

## Основная функция

Функция `main` предоставляет интерфейс командной строки для взаимодействия с библиотекой.

```python
def main():
    library = Library()

    while True:
        print("\nВыберите операцию:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книг")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        choice = input("Введите номер операции: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == "3":
            print("Выберите критерий поиска:")
            print("1. Название")
            print("2. Автор")
            print("3. Год издания")
            search_choice = input("Введите номер критерия поиска: ")

            if search_choice == "1":
                search_by = "Название"
            elif search_choice == "2":
                search_by = "Автор"
            elif search_choice == "3":
                search_by = "Год издания"
            else:
                print("Неверный выбор критерия поиска.")
                continue

            search_value = input(f"Введите значение для поиска по '{search_by}': ")
            results = library.search_books(**{search_by: search_value})

            if results:
                for book in results:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            print("Выберите новый статус:")
            print("1. В наличии")
            print("2. Выдана")
            status_choice = input("Введите номер нового статуса: ")
            if status_choice == "1":
                new_status = "в наличии"
            elif status_choice == "2":
                new_status = "выдана"
            else:
                print("Неверный выбор статуса.")
                continue
            library.change_status(book_id, new_status)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите корректный номер операции.")

if __name__ == "__main__":
    main()
```

## Запуск программы

Для запуска программы используйте команду:

```bash
python books.py
```

Эта команда запустит интерфейс командной строки, где вы сможете выполнять операции с книгами в библиотеке.

## Зависимости

- Python 3.x
- Модули `json` и `os` (входят в стандартную библиотеку Python)

