import unittest
import calc


class TestCalc(unittest.TestCase):
    """
    TestCalc class inherits from unittest.TestCase for creating unit tests for the calc library.
@@ -51,9 +52,25 @@ def test_add_string_and_number(self):
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

    def test_add_multiple_strings_and_number(self):
        """
        Test the addition of multiples strings and floats returns them as one
        concatenated string (in which the float is converted to a string).
        """
        result = calc.addAll(['abc', '5.5', 'def', '49'])
        self.assertEqual(result, 'abc5.5def49')

    def test_avoid(self):
        """
        Test if no arguments are passed to the addAll function.
        """
        result = calc.addAll([])
        self.assertEqual(result, '')


if __name__ == '__main__':
    '''
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
    unittest.main()
    The entry point for running the tests from the command line. The unittest.main() function
    uses a command-line interface and runs all the test methods whose names start with 'test'.
    '''
    unittest.main()
