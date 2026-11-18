"""Простой каталог книг с поиском автора без учета регистра."""
import argparse
import json
from pathlib import Path


DEFAULT_DATA = Path(__file__).with_name("books.json")


def load_books(path=DEFAULT_DATA):
    """Загрузить список книг из JSON-файла."""
    path = Path(path)
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Файл каталога должен содержать JSON-массив")
    return data


def search_by_author(books, author):
    """Найти книги по автору; регистр букв не учитывается."""
    query = author.strip()
    if not query:
        return []
    return [
        book for book in books
        if query in str(book.get("author", "")).casefold()
    ]


def main():
    parser = argparse.ArgumentParser(description="Поиск книг в учебном каталоге")
    parser.add_argument(
        "--data", default=str(DEFAULT_DATA),
        help="путь к JSON-файлу каталога (по умолчанию books.json)"
    )
    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser(
        "search-author", help="поиск книг по имени автора без учета регистра"
    )
    search_parser.add_argument("author", help="имя или часть имени автора")

    args = parser.parse_args()
    if args.command == "search-author":
        books = load_books(args.data)
        results = search_by_author(books, args.author)
        if results:
            for book in results:
                print(f'{book.get("title", "Без названия")} — {book.get("author", "Автор неизвестен")}')
        else:
            print("Книги не найдены")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
