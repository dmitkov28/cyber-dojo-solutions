import unittest
from solution import calculate_discount, find_all_combinations, find_combinations, find_max_discount


class TestHarryPotter(unittest.TestCase):
    def test_calculate_discount(self):
        result = calculate_discount(n_books=1)
        expected = 0
        self.assertEqual(result, expected)

        result = calculate_discount(n_books=2)
        expected = 2 * 8 * 0.05
        self.assertEqual(result, expected)

        result = calculate_discount(n_books=3)
        expected = 3 * 8 * 0.1
        self.assertEqual(result, expected)

        result = calculate_discount(n_books=4)
        expected = 4 * 8 * 0.2
        self.assertEqual(result, expected)

        result = calculate_discount(n_books=5)
        expected = 5 * 8 * 0.25
        self.assertEqual(result, expected)

    def test_find_combinations(self):
        books = [1, 1, 2, 2, 3, 3, 4, 5]
        expected_combinations_5 = [(1, 2, 3, 4, 5)]
        combinations_5 = find_combinations(books, n=5)
        self.assertEqual(sorted(expected_combinations_5), sorted(combinations_5))

        expected_combinations_4 = [
            (1, 3, 4, 5),
            (1, 2, 3, 5),
            (1, 2, 3, 4),
            (2, 3, 4, 5),
            (1, 2, 4, 5),
        ]

        combinations_4 = find_combinations(books, n=4)
        self.assertEqual(sorted(expected_combinations_4), sorted(combinations_4))

        expected_combinations_3 = [
            (2, 4, 5),
            (1, 3, 5),
            (1, 2, 3),
            (1, 3, 4),
            (2, 3, 5),
            (3, 4, 5),
            (2, 3, 4),
            (1, 2, 5),
            (1, 4, 5),
            (1, 2, 4),
        ]

        combinations_3 = find_combinations(books, n=3)
        self.assertEqual(sorted(expected_combinations_3), sorted(combinations_3))

        expected_combinations_2 = [
            (2, 4),
            (1, 2),
            (3, 4),
            (1, 5),
            (1, 4),
            (2, 3),
            (4, 5),
            (2, 5),
            (1, 3),
            (3, 5),
        ]

        combinations_2 = find_combinations(books, n=2)
        self.assertEqual(sorted(expected_combinations_2), sorted(combinations_2))

        expected_combinations_1 = [(2,), (5,), (4,), (1,), (3,)]
        combinations_1 = find_combinations(books, n=1)
        self.assertEqual(sorted(expected_combinations_1), sorted(combinations_1))

    def test_find_all_combinations(self):
        books = [1, 1, 2, 2, 3, 3, 4, 5]
        expected_combinations = [{5: 1, 3: 1}, {4: 2}, {3: 2, 2: 1}, {2: 4}]
        result = find_all_combinations(books)
        self.assertListEqual(expected_combinations, result)
        
    def test_find_max_discount(self):
        books = [1, 1, 2, 2, 3, 3, 4, 5]
        expected = {'group_size': 4, 'group_count': 2, 'discount': 12.8}
        
        groups = find_all_combinations(books)
        result = find_max_discount(groups)
        
        self.assertDictEqual(expected, result)
