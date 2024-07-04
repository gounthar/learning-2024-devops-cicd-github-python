import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.

    Methods:
    test_add_integers: Test that the addition of two integers returns the correct total.
    test_add_floats: Test that the addition of two floats returns the correct result.
    test_add_strings: Test the addition of two strings returns the two strings as one concatenated string.
    test_add_string_and_integer: Test the addition of a string and an integer returns them as one concatenated string.
    test_add_string_and_number: Test the addition of a string and a float returns them as one concatenated string.
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total.
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)
        
    def test_add_no_args(self):
        """
        Teste l'appel de add2 sans aucun argument. 
        Vérifie que la fonction renvoie 0 dans ce cas.
        """
        self.assertEqual(calc.add2(), 0)

    def test_add_one_arg(self):
        """
        Teste l'appel de add2 avec un seul argument.
        Vérifie que la fonction renvoie cet argument.
        """
        self.assertEqual(calc.add2(5), 5)

    def test_add_multiple_args(self):
        """
        Teste l'appel de add2 avec plusieurs arguments numériques.
        Vérifie que la fonction renvoie la somme de ces arguments.
        """
        self.assertEqual(calc.add2(2, 3, 4), 9)

    def test_add_string(self):
        """
        Teste l'appel de add2 avec des arguments mixtes, incluant des chaînes de caractères.
        Vérifie que la fonction additionne les nombres et ignore les chaînes de caractères.
        """
        self.assertEqual(calc.add2(2, 3, "bonjour"), 5)

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
