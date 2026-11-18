import unittest
from books import search_by_author, load_books


SAMPLE_BOOKS = [
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"title": "Собачье сердце", "author": "Михаил Булгаков"},
    {"title": "Идиот", "author": "Фёдор Достоевский"},
    {"title": "Война и мир", "author": "Лев Толстой"},
]


class TestAuthorSearch(unittest.TestCase):
    def test_author_search_ignores_case(self):
        self.assertEqual(len(search_by_author(SAMPLE_BOOKS, "михаил булгаков")), 2)

    def test_author_search_ignores_uppercase(self):
        self.assertEqual(len(search_by_author(SAMPLE_BOOKS, "МИХАИЛ БУЛГАКОВ")), 2)

    def test_author_search_partial_match(self):
        self.assertEqual(len(search_by_author(SAMPLE_BOOKS, "Булг")), 2)

    def test_author_search_exact_match(self):
        self.assertEqual(len(search_by_author(SAMPLE_BOOKS, "Лев Толстой")), 1)

    def test_author_search_not_found(self):
        self.assertEqual(search_by_author(SAMPLE_BOOKS, "Несуществующий автор"), [])

    def test_author_search_empty_query(self):
        self.assertEqual(search_by_author(SAMPLE_BOOKS, ""), [])

    def test_author_search_whitespace_query(self):
        self.assertEqual(search_by_author(SAMPLE_BOOKS, "   "), [])

    def test_author_search_strips_query(self):
        self.assertEqual(len(search_by_author(SAMPLE_BOOKS, "  Булгаков  ")), 2)

    def test_author_search_does_not_change_source(self):
        original = [dict(book) for book in SAMPLE_BOOKS]
        search_by_author(SAMPLE_BOOKS, "булгаков")
        self.assertEqual(SAMPLE_BOOKS, original)

    def test_author_search_missing_author_field(self):
        books = [{"title": "Без автора"}, {"title": "Есть автор", "author": "Иванов"}]
        self.assertEqual(search_by_author(books, "иванов"), [books[1]])

    def test_author_search_empty_catalog(self):
        self.assertEqual(search_by_author([], "Булгаков"), [])

    def test_example_catalog_loads(self):
        books = load_books("books.json.example")
        self.assertGreaterEqual(len(books), 1)


if __name__ == "__main__":
    unittest.main()
