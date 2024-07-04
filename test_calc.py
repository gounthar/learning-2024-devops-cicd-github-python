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

    def test_add_float_as_string(self):
        """
        Test that calling add with floating-point numbers as strings returns the concatenated result.
        """
        self.assertEqual(calc.add2("2.5", "3.7"), '2.53.7')

    def test_add_mixed_types(self):
        """
        Test that calling add with a mix of integers and floats returns the correct sum and concatenated result.
        """
        self.assertEqual(calc.add2(2, 3.5), 5.5)

    def test_add_empty_args(self):
        """
        Test that calling add with no arguments returns 0.
        """
        self.assertEqual(calc.add2(), 0)

    def test_add_large_numbers(self):
        """
        Test that calling add with large integers returns the correct sum.
        """
        self.assertEqual(calc.add2(1000000000000000000000000, 2000000000000000000000000), 3000000000000000000000000)

    def test_add_negative_numbers(self):
        """
        Test that calling add with negative numbers returns the correct sum.
        """
        self.assertEqual(calc.add2(-5, 10), 5)

if __name__ == '__main__':
    """
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    """
    unittest.main()
