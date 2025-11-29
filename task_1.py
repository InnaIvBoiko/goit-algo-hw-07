# Find the maximum value in the tree
def find_max_value(root):
    """
    Find the maximum value in the AVL tree.
    In a BST/AVL tree, the maximum value is always in the rightmost node.
    """
    if root is None:
        return None
    
    # Keep going right until we find the rightmost node
    current = root
    while current.right is not None:
        current = current.right
    
    return current.key