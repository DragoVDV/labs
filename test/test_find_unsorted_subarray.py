import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.calc2 import find_unsorted_subarray

class TestSorting(unittest.TestCase):
    
    def test_sorted_all(self):
        nums = [1,2,3,4,5,6]
        expect_result = (-1,-1)
        result  = find_unsorted_subarray(nums)
        self.assertEqual((result), (expect_result))
    
    def test_all_for_sorted(self):
        nums = [9,8,7,6,5,4,3,2,1]
        expept_result = (0,8)
        result = find_unsorted_subarray(nums)
        self.assertEqual((result),(expept_result))
    
    def test_one_element_sort(self):
        nums = [3]
        expect_result = (-1,-1)
        result = find_unsorted_subarray(nums)
        self.assertEqual((result), (expect_result))
        
      

if __name__ == '__main__':
    unittest.main()
