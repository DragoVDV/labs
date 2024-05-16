import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import unittest
from src.kruskal_mpt import read_csv,find_min_cable_length




class TestReadCSV(unittest.TestCase):

    def test_read_csv(self):
        test_csv_path = "../resources/communication_wells.csv"
        mst = read_csv(test_csv_path)
        connections = mst.get_connections()
        first_connection = connections[0]
        self.assertEqual(len(first_connection), 3)  

    def test_minimum_spanning_tree_algorithm(self):
        test_csv_path = "../resources/communication_wells.csv"
        mst = read_csv(test_csv_path)
        
        min_cable_length = find_min_cable_length(mst)
        self.assertEqual(min_cable_length, 7000)


    def test_unconnected_minimum_spanning_tree_algorithm(self):
        test_csv_path = "../resources/unconnected_wells.csv"
        mst = read_csv(test_csv_path)   
        
        min_cable_length = find_min_cable_length(mst)
        self.assertEqual(min_cable_length, -1)


if __name__ == '__main__':
    unittest.main()