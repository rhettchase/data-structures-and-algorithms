from data_structures.binary_tree import Node

def sum_files(node):
    if node is None:
        return 0
    if node.right is None and node.left is None:
        return 1
    else:
        return sum_files(node.left) + sum_files(node.right)

def compare_trees(tree1, tree2):
    tree1_count = sum_files(tree1)
    tree2_count = sum_files(tree2)
    if tree1_count == tree2_count:
        return True
    else:
        return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

file_count = sum_files(root)
print(f"Number of files: {file_count}")
