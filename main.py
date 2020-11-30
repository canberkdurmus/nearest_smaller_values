# Data structure to store a Cartesian tree node
class Node:
    def __init__(self, data, index=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.right_inherited = None
        self.left_inherited = None
        self.index = index


nodes = []


# Recursive function to perform inorder traversal of a Cartesian tree
def inorder_traversal(current_root):
    if current_root is None:
        return

    inorder_traversal(current_root.left)
    # print(current_root.data, end=' ')
    print(current_root.data, current_root.index)
    inorder_traversal(current_root.right)


def inorder_traversal_left(current_root, inherited):
    if current_root is None:
        return

    current_root.left_inherited = inherited
    # nsv_left = current_root.left_inherited

    # if nsv_left is None:
    #     print('-', end=' ')
    # else:
    #     print(inorder_array[nsv_left], end=' ')

    inorder_traversal_left(current_root.left, current_root.left_inherited)
    inorder_traversal_left(current_root.right, current_root.index)


def inorder_traversal_right(current_root, inherited):
    if current_root is None:
        return

    current_root.right_inherited = inherited
    # nsv_right = current_root.right_inherited

    # if nsv_right is None:
    #     print('-', end=' ')
    # else:
    #     print(inorder_array[nsv_right], end=' ')
    nodes.append(current_root)

    inorder_traversal_right(current_root.left, current_root.index)
    inorder_traversal_right(current_root.right, current_root.right_inherited)


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
    # print(index, start, end, '\t', inorder)
    current_root.index = index

    # recursively construct the left subtree
    current_root.left = construct_tree(inorder, start, index - 1)

    # recursively construct the right subtree
    current_root.right = construct_tree(inorder, index + 1, end)

    # return current node
    return current_root


if __name__ == '__main__':
    # input sequence of numbers representing the in-order sequence
    inorder_array = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]
    # inorder_array = [5, 10, 40, 30, 28]

    # construct the Cartesian tree
    root = construct_tree(inorder_array, 0, len(inorder_array) - 1)

    inorder_traversal_left(root, None)
    inorder_traversal_right(root, None)

    nodes.sort(key=lambda x: x.index, reverse=False)

    left_indices = []
    right_indices = []

    for n in nodes:
        left_indices.append(n.left_inherited)
        right_indices.append(n.right_inherited)

    print('Nearest Left Smaller Values: ', end=' ')
    for i in left_indices:
        if i is None:
            print('-', end=' ')
        else:
            print(inorder_array[i], end=' ')

    print('\nNearest Right Smaller Values:', end=' ')
    for i in right_indices:
        if i is None:
            print('-', end=' ')
        else:
            print(inorder_array[i], end=' ')
    print()
