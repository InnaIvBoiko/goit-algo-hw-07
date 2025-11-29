# AVL tree implementation from lecture notes
# Main file to demonstrate all three tasks

from task_1 import find_max_value
from task_2 import find_min_value  
from task_3 import find_sum_of_values

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def main():
    """Main function to demonstrate all three tasks"""
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    print("Building AVL Tree with values:", keys)
    for key in keys:
        root = insert(root, key)

    print("\nFinal AVL Tree:")
    print(root)

    # Test Task 1: Find maximum value
    max_value = find_max_value(root)
    print(f"Task 1 - Maximum value in the tree: {max_value}")

    # Test Task 2: Find minimum value
    min_value = find_min_value(root)
    print(f"Task 2 - Minimum value in the tree: {min_value}")

    # Test Task 3: Find sum of all values
    total_sum = find_sum_of_values(root)
    print(f"Task 3 - Sum of all values in the tree: {total_sum}")


if __name__ == "__main__":
    main()

