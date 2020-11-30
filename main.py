# Data structure to store a Cartesian tree node
class Node:
    def __init__(self, data, index=None, left=None, right=None):
        # Content of the node
        self.data = data
        # Right child of the node
        self.right = right
        # Left child of the node
        self.left = left
        # Inherited value with the right traversal
        self.right_inherited = None
        # Inherited value with the left traversal
        self.left_inherited = None
        # Index of the node in the inorder array
        self.index = index


# Variable is global because array is being filled by a recursive function
nodes = []


# Traversing the Cartesian Tree to find left smaller value for each node
def inorder_traversal_left(current_root, inherited):
    if current_root is None:
        return

    current_root.left_inherited = inherited

    inorder_traversal_left(current_root.left, current_root.left_inherited)
    inorder_traversal_left(current_root.right, current_root.index)


# Traversing the Cartesian Tree to find right smaller value for each node
def inorder_traversal_right(current_root, inherited):
    if current_root is None:
        return

    current_root.right_inherited = inherited
    nodes.append(current_root)

    inorder_traversal_right(current_root.left, current_root.index)
    inorder_traversal_right(current_root.right, current_root.right_inherited)


# Function to find the index of the minimum element in an array, to find root of the cartesian trees or subtrees
def min_element_index(inorder, start, end):
    min_index = start
    for i in range(start + 1, end + 1):
        if inorder[min_index] > inorder[i]:
            min_index = i

    return min_index


# Recursive function to construct the cartesian tree, builds tree as subtrees with starting and ending indices
def construct_tree(inorder, start, end):
    if start > end:
        return None

    index = min_element_index(inorder, start, end)
    current_root = Node(inorder[index])
    current_root.index = index

    current_root.left = construct_tree(inorder, start, index - 1)
    current_root.right = construct_tree(inorder, index + 1, end)

    return current_root


if __name__ == '__main__':
    # Name of the data file, integers must be divided by ', ' (comma and one whitespace)
    filename = 'data.txt'
    fileObject = open(filename, "r")
    data = fileObject.read()
    inorder_array = [int(i) for i in data.split(', ')]
    print('Array: ', inorder_array)

    root = construct_tree(inorder_array, 0, len(inorder_array) - 1)

    inorder_traversal_left(root, None)
    inorder_traversal_right(root, None)

    # Every node comes with it's smaller right and left nearest values but the sequence is unsorted so we sort them
    nodes.sort(key=lambda x: x.index, reverse=False)

    # Indices for the result array
    left_indices = []
    right_indices = []

    for n in nodes:
        left_indices.append(n.left_inherited)
        right_indices.append(n.right_inherited)

    # Printing the Nearest Smaller Values
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
