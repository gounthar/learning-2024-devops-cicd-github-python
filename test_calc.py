import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.
    """

    def test_add_without_args(self):
        """
        Test that calling add without arguments returns 0.
        """
        self.assertEqual(calc.add2(), 0)

    def test_add_arg(self):
        """
        Test that calling add with a single argument returns the argument itself.
        """
        self.assertEqual(calc.add2(5), 5)

    def test_add_many_args(self):
        """
        Test that calling add with multiple arguments returns the correct sum.
        """
        self.assertEqual(calc.add2(2, 3, 4), 9)

    def test_add_string(self):
        """
        Test that calling add with a mix of numbers and a string returns the concatenated result.
        """
        self.assertEqual(calc.add2(2, 3, "test"), '23test')

if __name__ == '__main__':
    """
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    """
    unittest.main()
