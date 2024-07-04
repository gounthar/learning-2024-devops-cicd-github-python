import unittest
from calc import add2

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_no_args: Test that calling add2 with no arguments returns 0.
    test_add_single_arg: Test that calling add2 with a single argument returns the argument itself.
    test_add_multiple_args: Test that calling add2 with multiple arguments returns their correct total.
    test_add_with_strings: Test the addition of numbers and strings returns them as one concatenated string.
    test_add_with_invalid_strings: Test the addition of numbers and invalid strings returns them as one concatenated string.
    """

    def test_add_no_args(self):
        """
        Test that calling add2 with no arguments returns 0.
        """
        self.assertEqual(add2(), 0)

    def test_add_single_arg(self):
        """
        Test that calling add2 with a single argument returns the argument itself.
        """
        self.assertEqual(add2(5), 5)

    def test_add_multiple_args(self):
        """
        Test that calling add2 with multiple arguments returns their correct total.
        """
        self.assertEqual(add2(1, 2, 3), 6)
        
    def test_add_with_strings(self):
        """
        Test the addition of numbers and strings returns them as one concatenated string.
        """
        self.assertEqual(add2(1, '2', 3), '123')
        
    def test_add_with_invalid_strings(self):
        """
        Test the addition of numbers and invalid strings returns them as one concatenated string.
        """
        self.assertEqual(add2(1, 'two', 3), '1two3')

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
