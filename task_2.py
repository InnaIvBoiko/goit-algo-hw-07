# Find the minimum value in the tree (Main focus of this file)
def find_min_value(root):
    """
    Find the minimum value in the AVL tree.
    In a BST/AVL tree, the minimum value is always in the leftmost node.
    """
    if root is None:
        return None
    
    # Keep going left until we find the leftmost node
    current = root
    while current.left is not None:
        current = current.left
    
    return current.key
