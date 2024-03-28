class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_tree_balanced(node):
    if node is None:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_tree_balanced(node.left) and is_tree_balanced(node.right)

