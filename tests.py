import pytest


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_check_book_added(self, collector):
        collector.add_new_book('Книга 1')
        assert 'Книга 1' in collector.get_books_rating() and len(collector.get_books_rating()) == 1

    def test_add_existing_book_book_not_added(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 1')
        assert collector.get_books_rating().get('Книга 1') == 1

    @pytest.mark.parametrize('book,rating', [('Book 1', 1), ('Book 2', 10)])
    def test_set_book_rating_at_border_values(self, collector, book, rating):
        collector.add_new_book(book)
        collector.set_book_rating(book, rating)
        assert collector.get_books_rating().get(book) == rating

    @pytest.mark.parametrize('book,rating', [('Book 1', 2), ('Book 2', 9)])
    def test_add_books_with_rating_within_borders(self, collector, book, rating):
        collector.add_new_book(book)
        collector.set_book_rating(book, rating)
        assert collector.get_books_rating().get(book) == rating

    @pytest.mark.parametrize('book,rating', [('Book 1', 0), ('Book 2', 11), ('Book 3', -1)])
    def test_set_rating_out_of_borders_not_applied(self, collector, book, rating):
        collector.add_new_book(book)
        collector.set_book_rating(book, rating)
        assert collector.get_book_rating(book) == 1

    def test_get_books_with_specific_rating(self, collector):
        for i in range(4):
            collector.add_new_book(f'Book {i}')
        for i in range(2):
            collector.set_book_rating(f'Book {i}', 9)
        assert len(collector.get_books_with_specific_rating(9)) == 2

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Book 3')
        collector.add_book_in_favorites('Book 3')
        assert 'Book 3' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Book 3')
        collector.add_book_in_favorites('Book 3')
        collector.delete_book_from_favorites('Book 3')
        assert 'Book 3' not in collector.get_list_of_favorites_books() \
               and len(collector.get_list_of_favorites_books()) == 0
