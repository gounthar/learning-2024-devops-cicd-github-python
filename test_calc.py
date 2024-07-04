import unittest
import calc


class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_integers: Test that the addition of two integers returns the correct total.
    test_add_floats: Test that the addition of two floats returns the correct result.
    test_add_float_and_int: Test that the addition of 1 integer and 1 float returns the correct total.
    test_add_floats_and_integers: Test that the addition of 1 integer and 1 float returns the correct total.
    test_add_floats_and_integers: Test that the addition of some integers and some floats returns the correct total.
    """

    LISTE_VALEUR = (1, 2, 3, 4)

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total.
        """
        result = calc.add((1, 2, 3, 4))
        self.assertEqual(result, 10)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct concac.
        """
        result = calc.add((1.5, 2.5))
        self.assertEqual(result, 4)

    def test_add_float_and_int(self):
        """
        Test that the addition of 1 integer and 1 float returns the correct total.
        """
        result = calc.add((1.5, 2))
        self.assertEqual(result, 3.5)

    def test_add_floats_and_integers(self):
        """
        Test that the addition of some integers and some floats returns the correct total.
        """
        result = calc.add((1.5, 2.5, 3, 3.5))
        self.assertEqual(result, 10.5)


if __name__ == "__main__":
    """
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    """
    unittest.main()
