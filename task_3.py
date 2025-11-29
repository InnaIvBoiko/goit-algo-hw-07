# Find the sum of all values in the tree (Main focus of this file)
def find_sum_of_values(root):
    """
    Find the sum of all values in the AVL tree using recursive traversal.
    """
    if root is None:
        return 0
    
    # Sum current node value + left subtree sum + right subtree sum
    return root.key + find_sum_of_values(root.left) + find_sum_of_values(root.right)
