import unittest
from tree import BinaryTree, is_tree_balanced

class TestBinaryTree(unittest.TestCase):
    def setUp(self):  
        
        self.root_balanced = BinaryTree(1)
        self.root_balanced.left = BinaryTree(2)
        self.root_balanced.right = BinaryTree(3)
        
        self.root_unbalanced = BinaryTree(1)
        self.root_unbalanced.left = BinaryTree(2)
        self.root_unbalanced.left.left = BinaryTree(3)
        self.root_unbalanced.left.left.left = BinaryTree(4)
        self.root_unbalanced.left.left.left.left = BinaryTree(5)
    
    def test_balanced_tree(self):
        self.assertTrue(is_tree_balanced(self.root_balanced))
    
    def test_unbalanced_tree(self):
        self.assertFalse(is_tree_balanced(self.root_unbalanced))

if __name__ == '__main__':
    unittest.main()
