# ./test_calc.py

import unittest
from calc import add2

class TestCalc(unittest.TestCase):

    def test_add_integers(self):
        result = add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = add2(10.5, 2)
        self.assertEqual(result, 12.5)  # Ensure float preservation

    def test_add_strings(self):
        result = add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        result = add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_strings_and_numbers(self):
        result = add2('abc', 5.5, 'def', 49)
        self.assertEqual(result, 'abc5.5def49')  # Ensure float as string

    def test_add_multiple_integers(self):
        result = add2(1, 2, 3)
        self.assertEqual(result, 6)

    def test_no_arguments(self):
        result = add2()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
