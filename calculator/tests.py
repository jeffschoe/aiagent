import unittest
from pkg.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("2 + 3"), 5)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("5 - 2"), 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("4 * 3"), 12)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("10 / 2"), 5)

    def test_complex_expression(self):
        self.assertEqual(self.calculator.evaluate("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(self.calculator.evaluate("( 2 + 3 ) * 4"), 20)

    def test_negative_numbers(self):
        self.assertEqual(self.calculator.evaluate("-2 + 5"), 3)

    def test_empty_expression(self):
        self.assertIsNone(self.calculator.evaluate(""))

    def test_invalid_token(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("2 + a")

    def test_new_test(self):
        self.assertEqual(self.calculator.evaluate("3 * 5 + 2"), 17)

if __name__ == '__main__':
    unittest.main()
