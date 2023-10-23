import unittest 

def is_even(number): 
  return number % 2 == 0 

class is_even_test(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2),"2 debe ser par")
    def test_is_odd(self):
        self.assertFalse(is_even(7), "7 no debe ser par")

if __name__ == '__main__':
    unittest.main()