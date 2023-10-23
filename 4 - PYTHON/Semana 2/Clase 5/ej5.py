import unittest

def count_words(text): 
  return len(text.split()) 
 
class TestCountWords(unittest.TestCase):
    def setUp(self):
        self.text = "This is a test"
    
    def test_count_words(self):
        self.assertEqual(count_words(self.text), 4)

if __name__ == "__main__":
    unittest.main()
    