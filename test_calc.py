import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    A test suite for validating the functionality of the `calc` library.

    This suite includes tests for various types of addition operations provided by the `calc` library, ensuring correct behavior across different data types and scenarios.

    Attributes:
        Inherits all attributes from unittest.TestCase, providing testing capabilities.

    Methods:
        test_add_integers: Verifies correct addition of two integers.
        test_add_floats: Checks addition of two floats for the correct result.
        test_add_strings: Ensures concatenation of two strings works as expected.
        test_add_string_and_integer: Tests concatenation of a string and an integer.
        test_add_string_and_number: Verifies concatenation of a string and a float.
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
        Test the addition of two strings returns the two strings as one concatenated string.
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one concatenated string (in which the integer is converted to a string).
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one concatenated string (in which the float is converted to a string).
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

    def test_add_no_args(self):
        """
        Test that calling add without arguments returns 0.
        """
        self.assertEqual(calc.add(), 0)

    def test_add_one_arg(self):
        """
        Test that calling add with a single argument returns the argument itself.
        """
        self.assertEqual(calc.add(5), 5)

    def test_add_multiple_args(self):
        self.assertEqual(calc.add(2, 3, 4), 9)

    def test_add_with_string(self):
        self.assertEqual(calc.add(2, 3, "hello"), 5)

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
