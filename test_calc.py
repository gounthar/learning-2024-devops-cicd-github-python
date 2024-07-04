import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    A test suite for validating the functionality of the `calc` library.

    This suite includes tests for various types of addition operations provided by the `calc` library, ensuring correct behavior across different data types and scenarios.

    Attributes:
        Inherits all attributes from unittest.TestCase, providing testing capabilities.

    Methods:
        test_add_without_args: Tests that calling add without arguments returns 0.
        test_add_one_arg: Checks that calling add with a single argument returns the argument itself.
        test_add_many_args: Tests addition of multiple arguments.
        test_add_plus_string: Ensures that adding a string to a number returns the sum.
    """

    def test_add_without_args(self):
        """
        Test that calling add without arguments return 0
        """
        self.assertEqual(calc.add2(), 0)

    def test_add_one_arg(self):
        """
        Test that calling add with a single argument returns the argument itself.
        """
        self.assertEqual(calc.add2(5), 5)

    def test_add_many_args(self):
        self.assertEqual(calc.add2(2, 3, 4), 9)

    def test_add_plus_string(self):
        self.assertEqual(calc.add2(2, 3, "hello"), 5)

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()