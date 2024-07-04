import unittest
import calc
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
    """
    def test_add2_no_args(self):
        self.assertEqual(add2(), 0)
        
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total.
        """
        self.assertEqual(add2(1, 2), 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result.
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string.
        """
        self.assertEqual(add2('hello', 'world'), 'helloworld')


    def test_add2_multiple_args(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string).
        """
        self.assertEqual(add2(1, 2, 3), 6)
        self.assertEqual(add2('a', 'b', 'c'), 'abc')
        self.assertEqual(add2(1, 'a', 2, 'b'), '1a2b')

    def test_add2_single_arg(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string).
        """
        self.assertEqual(add2(5), 5)
        self.assertEqual(add2('test'), 'test')


if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
