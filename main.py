# Data structure to store a Cartesian tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to perform inorder traversal of a Cartesian tree
def inorder_traversal(current_root):
    if current_root is None:
        return

    inorder_traversal(current_root.left)
    print(current_root.data, end=' ')
    inorder_traversal(current_root.right)


# Function to find index of the minimum element in inorder[start, end]
def min_element_index(inorder, start, end):
    min_index = start
    for i in range(start + 1, end + 1):
        if inorder[min_index] > inorder[i]:
            min_index = i

    return min_index


# Recursive function to construct a Cartesian tree from given
# inorder sequence
def construct_tree(inorder, start, end):
    # base case
    if start > end:
        return None

    # Find index of the minimum element in inorder[start, end]
    index = min_element_index(inorder, start, end)

    # The minimum element in given range of inorder sequence becomes the root
    current_root = Node(inorder[index])

    # recursively construct the left subtree
    current_root.left = construct_tree(inorder, start, index - 1)

    # recursively construct the right subtree
    current_root.right = construct_tree(inorder, index + 1, end)

    # return current node
    return current_root


if __name__ == '__main__':
    # input sequence of numbers representing the in-order sequence
    inorder = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]

    # construct the Cartesian tree
    root = construct_tree(inorder, 0, len(inorder) - 1)

    # print the Cartesian tree
    print("Inorder Traversal of constructed Cartesian tree is: ", end='')
    inorder_traversal(root)
