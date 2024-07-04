import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_integers: Test that the addition of two integers returns the correct total.
    test_add_floats: Test that the addition of two floats returns the correct result.
    test_add__many_integers: Test that the addition of two integers returns the correct total.
    test_add_many_floats: Test that the addition of two floats returns the correct result.
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total.
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add__many_integers(self):
        """
        Test that the addition of multiple integers returns the correct total.
        """
        result = calc.add2(1, 2, 7)
        self.assertEqual(result, 10)


    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result.
        """
        result = calc.add2(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add__many_floats(self):
        """
        Test that the addition of many floats returns the correct result.
        """
        result = calc.add2(10.5, 2, 5.5)
        self.assertEqual(result, 18)

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()