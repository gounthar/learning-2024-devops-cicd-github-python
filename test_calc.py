# ./test_calc.py

import unittest
from calc import add2

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_integers: Test that the addition of two integers returns the correct total.
    test_add_floats: Test that the addition of two floats returns the correct result.
    test_add_strings: Test the addition of two strings returns the two strings as one concatenated string.
    test_add_string_and_integer: Test the addition of a string and an integer returns them as one concatenated string.
    test_add_string_and_number: Test the addition of a string and a float returns them as one concatenated string.
    test_add_multiple_integers: Test that adding multiple integers returns the correct total.
    test_add_strings_and_numbers: Test the addition of multiple strings and numbers returns the correct concatenated result.
    test_no_arguments: Test if no arguments are passed to add2 function.
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total.
        """
        result = add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result.
        """
        result = add2(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string.
        """
        result = add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string).
        """
        result = add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_strings_and_numbers(self):
        """
        Test the addition of multiple strings and floats returns them as one
        concatenated string (in which the floats are converted to strings).
        """
        result = add2('abc', 5.5, 'def', 49)
        self.assertEqual(result, 'abc5.5def49')

    def test_add_multiple_integers(self):
        """
        Test that adding multiple integers returns the correct total.
        """
        result = add2(1, 2, 3)
        self.assertEqual(result, 6)

    def test_no_arguments(self):
        """
        Test if no arguments are passed to add2 function.
        """
        result = add2()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
