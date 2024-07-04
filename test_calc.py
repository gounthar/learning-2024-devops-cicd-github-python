import unittest
from calc import add2

class TestCalc(unittest.TestCase):
    """
    TestCalc class for creating unit tests for the calc library.
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
        
    def test_add_with_invalid_strings(self):
        """
        Test the addition of numbers and invalid strings returns them as one concatenated string.
        """
        self.assertEqual(add2(1, 'two', 3), '1two3')

if __name__ == '__main__':
    unittest.main()
