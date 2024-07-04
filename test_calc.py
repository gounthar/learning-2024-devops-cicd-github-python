import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_integers: Test that the addition of two integers returns the correct total.
    test_add_floats: Test that the addition of two floats returns the correct result.
    test_add_strings: Test the addition of two strings returns the two strings as one concatenated string.
    test_add_string_and_integers: Test the addition of a string and an integer returns them as one concatenated string.
    test_add_string_and_numbers: Test the addition of a string and a float returns them as one concatenated string.
    test_add_one_int: Test the addition of a single integer returns it as the same integer.
    test_add_one_string: Test the addition of a single string returns it as the same string.
    test_add_one_float: Test the addition of a single float returns it as the same float.
    test_add_nothing: Test the addition of nothing returns 0.
    """

    def test_add_integers(self):
        """
        Test that the addition of three integers returns the correct total.
        """
        result = calc.add(1, 2, 3)
        self.assertEqual(result, 6)

    def test_add_floats(self):
        """
        Test that the addition of three floats returns the correct result.
        """
        result = calc.add('10.5', 2, '2.4')
        self.assertEqual(result, 14.9)

    def test_add_strings(self):
        """
        Test the addition of four strings returns the four strings as one
        concatenated string.
        """
        result = calc.add('abc', 'def', 'ghi', 'jkl')
        self.assertEqual(result, 'abcdefghijkl')

    def test_add_string_and_integers(self):
        """
        Test the addition of a string and two integers returns them as one
        concatenated string (in which the integers are converted to a string).
        """
        result = calc.add('abc', 3, 57)
        self.assertEqual(result, 'abc357')

    def test_add_string_and_numbers(self):
        """
        Test the addition of a string, a float and a integer returns them as one
        concatenated string (in which the float and the  is converted to a string).
        """
        result = calc.add('abc', '5.5', 5)
        self.assertEqual(result, 'abc5.55')

    def test_add_one_int(self):
        """
        Test the addition of an integer returns as the same integer.
        """
        result = calc.add(5)
        self.assertEqual(result, 5)

    def test_add_one_string(self):
        """
        Test the addition of an string returns as the same string.
        """
        result = calc.add('salut')
        self.assertEqual(result, 'salut')

    def test_add_one_float(self):
        """
        Test the addition of an float returns as the same float.
        """
        result = calc.add('0.75')
        self.assertEqual(result, 0.75)

    def test_add_nothing(self):
        """
        Test the addition of nothing returns 0.
        """
        result = calc.add()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
