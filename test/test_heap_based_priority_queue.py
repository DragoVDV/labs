import unittest
from heap_based_priority_queue import BinaryHeap

class TestBinaryHeap(unittest.TestCase):
    def setUp(self):
        self.heap = BinaryHeap()

    def test_add_element(self):
        self.heap.add_element('Task 2', 2)
        self.heap.add_element('Task 3', 4)
        self.heap.add_element('Task 4', 1)
        self.heap.add_element('Task 5', 7)
        self.heap.add_element('Task 6', 11)
        self.heap.add_element('Task 7', 3)
        self.assertEqual(self.heap.priority_queue[0].priority, 11)

    def test_no_data(self):
        self.assertEqual(len(self.heap.priority_queue), 0)

    def test_equality_element(self):      
        self.heap.add_element('Task 2', 1)
        self.heap.add_element('Task 3', 1)
        self.heap.add_element('Task 4', 1)
        self.heap.add_element('Task 5', 1)
        self.heap.add_element('Task 6', 1)
        self.heap.add_element('Task 7', 2)
        self.heap.pop_element()
        self.assertEqual(self.heap.priority_queue[0].priority, 1)


    
if __name__ == '__main__':
    unittest.main()
