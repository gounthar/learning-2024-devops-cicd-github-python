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

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result.
        """
        result = calc.add2(10.5, 2)
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

    def test_add_multiple_numbers(self):
        """
        Teste que l'addition de plusieurs nombres entiers donne le résultat correct.
        Ce test passe quatre entiers a la fonction add2 et vérifie que la somme est égale à 10.
        """
        self.assertEqual(calc.add2(1, 2, 3, 4), 10)

    def test_add_no_arguments(self):
        """
        Teste que l'addition sans arguments renvoie 0.
        Ce test vérifie que la fonction add2 peut gérer l'appel sans argument et renvoie la valeur 0.
        """
        self.assertEqual(calc.add2(), 0)

    def test_add_single_argument(self):
        """
        Teste que l'addition d'un seul argument renvoie cet argument.
        Ce test passe un seul entier à la fonction add2 et vérifie que la sortie est la même que l'entrée.
        """
        self.assertEqual(calc.add2(5), 5)

    def test_add_mixed_types(self):
        """
        Test l'addition de types mixte pour vérifié la concaténation.
        Ce test passe un entier, une chaîne de caractères et un flottant à la fonction add2 et vérifie
        que les valeurs sont correctement concaténées en une seule chaîne de caractères.
        """
        self.assertEqual(calc.add2(1, 'a', 3.5), '1a3.5')

if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
