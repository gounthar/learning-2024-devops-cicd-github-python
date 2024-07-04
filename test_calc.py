import unittest
from calc import add2

class TestCalc(unittest.TestCase):

    def test_add2_no_arguments(self):
        self.assertEqual(add2(), 0, "Should return 0 when no arguments are provided")

    def test_add2_single_argument(self):
        self.assertEqual(add2(5), 5, "Should return the single argument itself")
        self.assertEqual(add2("hello"), "hello", "Should return the single string argument itself")

    def test_add2_multiple_numeric_arguments(self):
        self.assertEqual(add2(1, 2, 3), 6, "Should return the sum of numeric arguments")
        self.assertEqual(add2(1.5, 2.5), 4.0, "Should return the sum of float arguments")
        self.assertEqual(add2(1, 2.5, 3), 6.5, "Should handle a mix of int and float arguments")

    def test_add2_multiple_string_arguments(self):
        self.assertEqual(add2("hello", " ", "world"), "hello world", "Should concatenate string arguments")

    def test_add2_mixed_arguments(self):
        self.assertEqual(add2(1, "apple", 2), "1apple2", "Should concatenate all arguments as strings when at least one is a string")
        self.assertEqual(add2("foo", 1, 2.5), "foo12.5", "Should concatenate all arguments as strings when the first is a string")
        self.assertEqual(add2(1, 2, "3"), "33", "Should concatenate all arguments as strings when the last is a string")

if __name__ == '__main__':
    unittest.main()