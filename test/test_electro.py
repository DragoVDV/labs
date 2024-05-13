import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.electro import find_total_wire_length, read_txt, write_txt

class TestFindTotalWireLength(unittest.TestCase):
    def test_first_scenario(self):
        input_file_path = "resources/electro_input1.txt"
        expected_output_file_path = "resources/electro_output1.txt"
        expected_result = 5.66  

        distance_between_poles, heights = read_txt(input_file_path)
        result = find_total_wire_length(distance_between_poles, heights)

        self.assertAlmostEqual(result, expected_result, places=2)

        write_txt(expected_output_file_path, result)
    def test_second_scenario(self):
        input_file_path = "resources/electro_input2.txt"
        expected_output_file_path = "resources/electro_output2.txt"
        expected_result = 300

        distance_between_poles, heights = read_txt(input_file_path)
        result = find_total_wire_length(distance_between_poles, heights)

        self.assertAlmostEqual(result, expected_result, places=2)

        write_txt(expected_output_file_path, result)


    def test_third_scenario(self):
        input_file_path = "resources/electro_input3.txt"
        expected_output_file_path = "resources/electro_output3.txt"
        expected_result = 396.32

        distance_between_poles, heights = read_txt(input_file_path)
        result = find_total_wire_length(distance_between_poles, heights)

        self.assertAlmostEqual(result, expected_result, places=2)

        write_txt(expected_output_file_path, result)
        
      

    


if __name__ == '__main__':
    unittest.main()