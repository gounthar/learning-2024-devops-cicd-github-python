import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    La classe TestCalc hérite de unittest.TestCase pour créer des tests unitaires pour la bibliothèque calc.

    Méthodes:
    test_add_integers: Tester que l'addition de deux entiers renvoie le total correct.
    test_add_floats: Tester que l'addition de deux floats renvoie le résultat correct.
    test_add_strings: Tester que l'addition de deux chaînes renvoie les deux chaînes concaténées.
    test_add_string_and_integer: Tester que l'addition d'une chaîne et d'un entier les concatène en une seule chaîne.
    test_add_string_and_number: Tester que l'addition d'une chaîne et d'un float les concatène en une seule chaîne.
    test_add_no_arguments: Tester la fonction d'addition sans arguments.
    test_add_single_argument: Tester la fonction d'addition avec un seul argument.
    test_add_multiple_arguments: Tester la fonction d'addition avec plusieurs arguments.
    test_add_mixed_arguments: Tester la fonction d'addition avec des types d'arguments mixtes.
    """

    def test_add_integers(self):
        """
        Tester que l'addition de deux entiers renvoie le total correct.
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Tester que l'addition de deux floats renvoie le résultat correct.
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Tester que l'addition de deux chaînes renvoie les deux chaînes concaténées.
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Tester que l'addition d'une chaîne et d'un entier les concatène en une seule chaîne
        (où l'entier est converti en chaîne).
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Tester que l'addition d'une chaîne et d'un float les concatène en une seule chaîne
        (où le float est converti en chaîne).
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

    def test_add_no_arguments(self):
        """
        Tester la fonction d'addition sans arguments.
        """
        result = calc.add2()
        self.assertEqual(result, '')

    def test_add_single_argument(self):
        """
        Tester la fonction d'addition avec un seul argument.
        """
        result = calc.add2(5)
        self.assertEqual(result, 5)

    def test_add_multiple_arguments(self):
        """
        Tester la fonction d'addition avec plusieurs arguments.
        """
        result = calc.add2(1, 2, 3, 4)
        self.assertEqual(result, 10)

    def test_add_mixed_arguments(self):
        """
        Tester la fonction d'addition avec des types d'arguments mixtes.
        """
        result = calc.add2(1, '2', 3.0, '4')
        self.assertEqual(result, '123.04')

    if __name__ == '__main__':
        '''
        Le point d'entrée pour exécuter les tests depuis la ligne de commande. La fonction unittest.main()
        utilise une interface en ligne de commande et exécute toutes les méthodes de test dont le nom commence par 'test'.
        '''
    unittest.main()
