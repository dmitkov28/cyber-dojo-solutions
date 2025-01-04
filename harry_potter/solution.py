import itertools
from typing import List


def calculate_discount(n_books: int) -> float:
    SINGLE_BOOK_PRICE = 8
    SINGLE_BOOK_DISCOUNT_RATE = 0
    TWO_BOOKS_DISCOUNT_RATE = 0.05
    THREE_BOOKS_DISCOUNT_RATE = 0.1
    FOUR_BOOKS_DISCOUNT_RATE = 0.2
    FIVE_BOOKS_DISCOUNT_RATE = 0.25

    if n_books == 1:
        return n_books * SINGLE_BOOK_PRICE * SINGLE_BOOK_DISCOUNT_RATE

    if n_books == 2:
        return n_books * SINGLE_BOOK_PRICE * TWO_BOOKS_DISCOUNT_RATE

    if n_books == 3:
        return n_books * SINGLE_BOOK_PRICE * THREE_BOOKS_DISCOUNT_RATE

    if n_books == 4:
        return n_books * SINGLE_BOOK_PRICE * FOUR_BOOKS_DISCOUNT_RATE

    if n_books == 5:
        return n_books * SINGLE_BOOK_PRICE * FIVE_BOOKS_DISCOUNT_RATE


def has_possible_combinations(input_data: List[int], n_combinations: int) -> bool:
    return len(set(itertools.combinations(input_data, n_combinations))) > 0


def remove_book(books: List[int], book_to_remove: int) -> List[int]:
    new_books = books.copy()
    new_books.remove(book_to_remove)
    return new_books
