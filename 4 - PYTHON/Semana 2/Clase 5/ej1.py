import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(1,2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = self.calculator.subtract(1,2)
        self.assertEqual(result, -1)

    def test_multiply(self):
        result = self.calculator.multiply(1,2)
        self.assertEqual(result, 2)

    def test_divide(self):
        result = self.calculator.divide(1,2)
        self.assertEqual(result, 0.5)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
