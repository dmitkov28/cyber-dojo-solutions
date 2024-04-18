import unittest
from solution import check


class TestCheck(unittest.TestCase):
    def test_should_return_Fizz_when_given_multiples_of_3(self):
        self.assertEqual("Fizz", check(3))
        self.assertEqual("Fizz", check(6))
        self.assertEqual("Fizz", check(9))
        self.assertEqual("Fizz", check(99))
        self.assertEqual("Fizz", check(123))

    def test_should_return_Buzz_given_multiples_of_5(self):
        self.assertEqual("Buzz", check(5))
        self.assertEqual("Buzz", check(10))
        self.assertEqual("Buzz", check(25))
        self.assertEqual("Buzz", check(55))
        self.assertEqual("Buzz", check(175))

    def test_should_return_FizzBuzz_given_multiples_of_3_and_5(self):
        self.assertEqual("FizzBuzz", check(15))
        self.assertEqual("FizzBuzz", check(30))
        self.assertEqual("FizzBuzz", check(45))
        self.assertEqual("FizzBuzz", check(120))
        self.assertEqual("FizzBuzz", check(540))

    def test_should_return_number_in_any_other_case(self):
        self.assertEqual("7", check(7))
        self.assertEqual("19", check(19))
        self.assertEqual("122", check(122))
        self.assertEqual("374", check(374))
        self.assertEqual("1001", check(1001))
