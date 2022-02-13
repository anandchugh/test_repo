import unittest
from main import sum

class Testing(unittest.TestCase):
    def test_1(self):
        result = sum(2,3)
        self.assertEqual(result, 5)

    def test_2(self):
        result = sum(1,2)
        self.assertEqual(result, 3)

    
    def test_3(self):
        result = sum(1,2)
        self.assertEqual(result, 5)
        
if __name__ == '__main__':
    unittest.main()