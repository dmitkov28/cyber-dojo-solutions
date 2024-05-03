import unittest
from solution import generate_anagrams


class TestCheck(unittest.TestCase):
    def test_should_return_list_of_anagrams(self):
        self.assertListEqual(["ab", "ba"], generate_anagrams("ab"))
        self.assertListEqual(
            sorted(["abc", "acb", "bac", "bca", "cba", "cab"]),
            sorted(generate_anagrams("abc")),
        )
