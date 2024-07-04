import unittest
import calc

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

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total.
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

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
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string).
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string).
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

    def test_add_multiple_numbers(self):
        """
        Test the addition of multiple integers and floats to ensure the correct total is returned.
        """
        result = calc.add2(1, 2, 3, 4)
        self.assertEqual(result, 10)
        result = calc.add2(1.1, 2.2, 3.3)
        self.assertEqual(result, 6.6)

    def test_add_mixed_types_multiple(self):
        """
        Test the addition of a combination of strings, integers, and floats.
        This should concatenate everything into a single string.
        """
        result = calc.add2('hello', 1, 2.2, 'world')
        self.assertEqual(result, 'hello12.2world')

    def test_add_variable_arguments(self):
        """
        Test the function with no arguments and with one argument to verify that it handles these cases correctly.
        """
        self.assertEqual(calc.add2(), 0)
        self.assertEqual(calc.add2(5), 5)
        self.assertEqual(calc.add2('test'), 'test')


if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
