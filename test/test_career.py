import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.career import *

class Test_correct(unittest.TestCase):

    def test_correct(self):
        input_file = 'C:/Workspace/python/labs/resources/career1_input'
        output_file = 'C:/Workspace/python/labs/resources/career1_output'
        max_experience(input_file, output_file)

        with open(output_file, 'r') as file:
            result = file.read().strip()

        expected_result = '12'  

        self.assertEqual(result, expected_result)

    def test_zero(self):
        input_file = 'C:/Workspace/python/labs/resources/career2_input'
        output_file = 'C:/Workspace/python/labs/resources/career2_output'
        max_experience(input_file, output_file)

        with open(output_file, 'r') as file:
            result = file.read().strip()

        expected_result = '0'  

        self.assertEqual(result, expected_result)

    def test_negative(self):
        input_file = 'C:/Workspace/python/labs/resources/career3_input'
        output_file = 'C:/Workspace/python/labs/resources/career3_output'
        max_experience(input_file, output_file)

        with open(output_file, 'r') as file:
            result = file.read().strip()

        expected_result = '-5'  

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
