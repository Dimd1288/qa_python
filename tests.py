import pytest

BOOKS = ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5', 'Book 6', 'Book 7', 'Book 8', 'Book 9', 'Book 10']
RATINGS = [('Book 1', 1),
           ('Book 2', 2),
           ('Book 3', 3),
           ('Book 4', 4),
           ('Book 5', 5),
           ('Book 6', 6),
           ('Book 7', 7),
           ('Book 8', 8),
           ('Book 9', 9),
           ('Book 10', 10)]


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_check_book_added(self, collector):
        collector.add_new_book('Книга 1')
        assert collector.get_books_rating().get('Книга 1') == 1

    def test_add_existing_book_book_not_added(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 1')
        assert collector.get_books_rating().get('Книга 1') == 1

    def test_set_book_rating(self, collector):
        collector.add_new_book('Книга 1')
        collector.set_book_rating('Книга 1', 10)
        assert collector.get_book_rating('Книга 1') == 10

    @pytest.mark.parametrize('books, ratings', RATINGS)
    def test_add_books_with_ratings_from_1_to_10(self, collector, books, ratings):
        for book in BOOKS:
            collector.add_new_book(book)
            collector.set_book_rating(book, len(collector.get_books_rating()))
        assert collector.get_books_rating().get(books) == ratings

    def test_set_rating_less_than_1_is_not_applied(self, collector):
        collector.add_new_book('Book 1')
        collector.set_book_rating('Book 1', 0)
        assert collector.get_book_rating('Book 1') == 1

    def test_set_rating_more_than_10_is_not_applied(self, collector):
        collector.add_new_book('Book 1')
        collector.set_book_rating('Book 1', 11)
        assert collector.get_book_rating('Book 1') == 1

    def test_get_books_with_specific_rating(self, collector):
        for i in range(6):
            collector.add_new_book(f'Book {i}')
        for i in range(3):
            collector.set_book_rating(f'Book {i}', 9)
        assert len(collector.get_books_with_specific_rating(9)) == 3

    def test_add_book_in_favorites(self, collector):
        for i in range(6):
            collector.add_new_book(f'Book {i}')
        for i in range(3, 6):
            collector.add_book_in_favorites(f'Book {i}')
        assert len(collector.get_list_of_favorites_books()) == 3

    def test_delete_book_from_favorites(self, collector):
        for i in range(6):
            collector.add_new_book(f'Book {i}')
        for i in range(3, 6):
            collector.add_book_in_favorites(f'Book {i}')
        collector.delete_book_from_favorites('Book 4')
        assert 'Book 4' not in collector.get_list_of_favorites_books() \
               and len(collector.get_list_of_favorites_books()) == 2