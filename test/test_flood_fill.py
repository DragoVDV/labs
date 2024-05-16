import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.flood_fill import *

class TestFloodFill(unittest.TestCase):

    def test_correct(self):
        input_file = '../resources/input1.txt'
        output_file = '../resources/output1.txt'
        flood_fill(input_file, output_file)

        expected_matrix = [
            ['Y', 'Y', 'Y', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'L', 'X', 'X', 'X'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'L', 'L', 'L', 'L', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'L', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'L', 'L', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'Y', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]

        with open(output_file, 'r') as file:
            result_matrix = [list(eval(line.strip())) for line in file]

        self.assertEqual(result_matrix, expected_matrix)

  
    def test_out_of_range_error(self):
        with self.assertRaises(ValueError):
         input_file = '../resources/input2.txt'
         output_file = '../resources/output2.txt'
         flood_fill(input_file, output_file)
    


    def test_same_points(self):
        input_file = '../resources/input3.txt'
        output_file = '../resources/output3.txt'
        flood_fill(input_file, output_file)
        expected_matrix = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['C', 'C', 'C', 'C', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'Y', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

        ]
        with open(output_file, 'r') as file:
                result_matrix = [list(eval(line.strip())) for line in file]

        self.assertEqual(result_matrix, expected_matrix)
if __name__ == '__main__':
    unittest.main()
