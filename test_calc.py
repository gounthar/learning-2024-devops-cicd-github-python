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
    Test that the addition of multiple arguments returns the correct total or concatenated string.
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total.
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result.
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string.
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string).
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string).
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')
    
    def test_multiple_arguments(self):
        """
        Test that the addition of multiple arguments returns the correct total or concatenated string.
        """
        # Teste l'addition de plusieurs arguments entiers
        result = calc.add2(1, 2, 3)
        # Vérifie que le résultat est la somme correcte des entiers
        self.assertEqual(result, 6)
    
        # Teste l'addition d'arguments mixtes avec des flottants et un entier
        result = calc.add2(1.5, 2.5, 3)
        # Vérifie que le résultat est la somme correcte des flottants et de l'entier
        self.assertEqual(result, 7.0)
    
        # Teste la concaténation de plusieurs arguments de type chaîne
        result = calc.add2('a', 'b', 'c')
        # Vérifie que le résultat est la concaténation correcte des chaînes
        self.assertEqual(result, 'abc')
    
        # Teste des types mixtes avec des entiers et une chaîne
        result = calc.add2(1, 'b', 3)
        # Vérifie que le résultat est la concaténation correcte, convertissant tous les arguments en chaînes
        self.assertEqual(result, '1b3')

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
