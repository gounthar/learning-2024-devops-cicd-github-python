import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_no_args: Test that calling add2 without any arguments returns 0.
    test_add_one_arg: Test that calling add2 with a single argument (5) returns 5.
    test_add_multiple_args: Test that calling add2 with multiple integer arguments returns their sum.
    test_add_with_string: Test that calling add2 with mixed types (integers and strings) returns the correct result.
    """

    def test_add_no_args(self):
        """
        Test that calling add2 without any arguments returns 0.
        """
        self.assertEqual(calc.add2(), 0)

    def test_add_one_arg(self):
        """
        Test that calling add2 with a single argument (5) returns 5.
        """
        self.assertEqual(calc.add2(5), 5)

    def test_add_multiple_args(self):
        """
        Test that calling add2 with multiple integer arguments (2, 3, 4) returns their sum (9).
        """
        self.assertEqual(calc.add2(2, 3, 4), 9)

    def test_add_with_string(self):
        """
        Test that calling add2 with mixed types (integers and a string) returns the correct result.
        If a string is included, the integers are converted to strings and concatenated.
        """
        self.assertEqual(calc.add2(2, 3, "hello"), '5hello')

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
