import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.amout import size_m

class TestSizeM(unittest.TestCase):
    
    def test_standart(self):
        result = size_m(10, 2, 3)
        self.assertEqual(result, 9)

    def test_bix_num(self):
        result = size_m(2, 1000000000, 999999999)
        self.assertEqual(result, 1999999998)

    def test_square(self):
        result = size_m(4, 1, 1)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
