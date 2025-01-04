from typing import List
import unittest
from solution import calculate_discount


class TestHarryPotter(unittest.TestCase):
    def test_calculate_discount(self):
        SINGLE_BOOK_DISCOUNT_RATE = 0
        TWO_BOOKS_DISCOUNT_RATE = 0.05
        THREE_BOOKS_DISCOUNT_RATE = 0.1
        FOUR_BOOKS_DISCOUNT_RATE = 0.2
        FIVE_BOOKS_DISCOUNT_RATE = 0.25

        single_book_discount = calculate_discount(n_books=1)
        two_books_discount = calculate_discount(n_books=2)
        three_books_discount = calculate_discount(n_books=3)
        four_books_discount = calculate_discount(n_books=4)
        five_books_discount = calculate_discount(n_books=5)

        self.assertEqual(single_book_discount, (SINGLE_BOOK_DISCOUNT_RATE + 1))
        self.assertEqual(two_books_discount, (TWO_BOOKS_DISCOUNT_RATE + 1) * 2)
        self.assertEqual(three_books_discount, (THREE_BOOKS_DISCOUNT_RATE + 1) * 3)
        self.assertEqual(four_books_discount, (FOUR_BOOKS_DISCOUNT_RATE + 1) * 4)
        self.assertEqual(five_books_discount, (FIVE_BOOKS_DISCOUNT_RATE + 1) * 5)

    def test_has_possible_combinations(self):
        input_data = [1, 1, 2, 2, 3, 3, 4, 5]

        has_combinations_of_1 = has_possible_combinations(input_data, 1)
        self.assertTrue(has_combinations_of_1)

        has_combinations_of_2 = has_possible_combinations(input_data, 2)
        self.assertTrue(has_combinations_of_2)

        has_combinations_of_3 = has_possible_combinations(input_data, 3)
        self.assertTrue(has_combinations_of_3)

        has_combinations_of_4 = has_possible_combinations(input_data, 4)
        self.assertTrue(has_combinations_of_4)

        has_combinations_of_5 = has_possible_combinations(input_data, 5)
        self.assertTrue(has_combinations_of_5)

        input_data = [1, 2]

        has_combinations_of_2 = has_possible_combinations(input_data, 3)
        self.assertFalse(has_combinations_of_2)

        input_data = [1]

        has_combinations_of_2 = has_possible_combinations(input_data, 2)
        self.assertFalse(has_combinations_of_2)
