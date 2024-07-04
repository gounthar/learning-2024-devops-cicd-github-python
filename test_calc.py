import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    Tests for validating the functionality of the `calc` file.
    
    Methods:
    test_add_no_args: Test that calling add without arguments returns 0.
    test_add_one_arg: Test that calling add with a single argument returns the argument itself.
    test_add_multiple_args: Test the addition of multiple args returns addition of them all.
    test_add_with_string: Test the addition of a string and other args returns them as addition of them all without paying attention to string.
    """
    
    def test_add_no_args(self):
        self.assertEqual(calc.add2(), 0)

    def test_add_one_arg(self):
        self.assertEqual(calc.add2(5), 5)

    def test_add_multiple_args(self):
        self.assertEqual(calc.add2(2, 3, 4), 9)

    def test_add_with_string(self):
        self.assertEqual(calc.add2(2, 3, "hello"), 5)


if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
