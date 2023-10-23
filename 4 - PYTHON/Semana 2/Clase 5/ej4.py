import unittest


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


class testTemperature(unittest.TestCase):
    def setUp(self):
        self.fahrenheit = 100
        self.celsius = 37.78

    def test_celsius_to_fahrenheit(self):
        result = celsius_to_fahrenheit(self.celsius)
        self.assertAlmostEqual(result, self.fahrenheit, places = 2)

if __name__ == "__main__":
    unittest.main()
