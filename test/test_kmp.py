import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
from src.kmp import *



class TestKMP(unittest.TestCase):
    def test_build_prefix_table(self):
        self.assertEqual(build_prefix_table("ABABCAB"), [0, 0, 1, 2, 0, 1, 2])

    def test_kmp_search(self):
        haystack = "ABABDABACDABABCABAB"
        needle = "AB"
        self.assertEqual(kmp_search(haystack, needle), [0, 2, 5, 10, 12, 15, 17])

    def test_kmp_search_no_matches(self):
        haystack = "ABABDABACDABABCABAB"
        needle = "XYZ"
        self.assertEqual(kmp_search(haystack, needle), [])

if __name__ == '__main__':
    unittest.main()
