import unittest
from calc import add2

class TestCalc(unittest.TestCase):
    def test_add_no_args(self):
        self.assertEqual(add2(), 0)

    def test_add_single_arg(self):
        self.assertEqual(add2(5), 5)

    def test_add_multiple_args(self):
        self.assertEqual(add2(1, 2, 3), 6)
    
    def test_add_with_strings(self):
        self.assertEqual(add2(1, '2', 3), '123')
    
    def test_add_with_invalid_strings(self):
        self.assertEqual(add2(1, 'two', 3), '1two3')

if __name__ == '__main__':
    unittest.main()
