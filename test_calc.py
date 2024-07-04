import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_integers: Test that the addition of integers returns the correct total.
    test_add_floats: Test that the addition of floats returns the correct result.
    test_add_strings: Test the addition of strings returns them as one concatenated string.
    test_add_string_and_integer: Test the addition of a string and an integer returns them as one concatenated string.
    test_add_string_and_number: Test the addition of a string and a float returns them as one concatenated string.
    test_add_no_args: Test that calling add2 with no arguments returns None.
    test_add_one_arg: Test that calling add2 with one argument returns that argument.
    test_add_mixed_args: Test the addition of mixed types returns the correct result.
    """

    def test_add_integers(self):
        """
        Test that the addition of integers returns the correct total.
        """
        result = calc.add2(1, 2, 3, 4)
        self.assertEqual(result, 10)

    def test_add_floats(self):
        """
        Test that the addition of floats returns the correct result.
        """
        result = calc.add2('10.5', 2, 3.5)
        self.assertEqual(result, 16.0)

    def test_add_strings(self):
        """
        Test the addition of strings returns them as one concatenated string.
        """
        result = calc.add2('abc', 'def', 'ghi')
        self.assertEqual(result, 'abcdefghi')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one concatenated string (in which the integer is converted to a string).
        """
        result = calc.add2('abc', 3, 'def')
        self.assertEqual(result, 'abc3def')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one concatenated string (in which the float is converted to a string).
        """
        result = calc.add2('abc', '5.5', 7.5)
        self.assertEqual(result, 'abc5.57.5')

    def test_add_no_args(self):
        """
        Test that calling add2 with no arguments returns None.
        """
        result = calc.add2()
        self.assertIsNone(result)

    def test_add_one_arg(self):
        """
        Test that calling add2 with one argument returns that argument.
        """
        result = calc.add2(5)
        self.assertEqual(result, 5)

    def test_add_mixed_args(self):
        """
        Test the addition of mixed types returns the correct result.
        """
        result = calc.add2(1, '2', 3.0)
        self.assertEqual(result, '123.0')

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
