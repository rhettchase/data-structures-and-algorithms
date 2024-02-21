from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

# ITERATIVE METHOD

def tree_intersection(tree1, tree2):
    hashtable_for_tree1 = Hashtable()
    matches = set()

    # Populate the hashtable with values from the first binary tree using iterative traversal
    _traverse_and_set_values_iterative(tree1.root, hashtable_for_tree1)

    # Traverse the second binary tree and find matches using iterative traversal
    _find_matches_iterative(tree2.root, hashtable_for_tree1, matches)

    return matches

def _find_matches_iterative(root, hashtable, matches):
    if not root:
        return
    stack = [root]
    while stack:
        current_node = stack.pop()
        if hashtable.has(current_node.value):
            matches.add(current_node.value)
        # Note: Right child is pushed first so that the left child is processed first
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

def _traverse_and_set_values_iterative(root, hashtable):
    if not root:
        return
    stack = [root]
    while stack:
        current_node = stack.pop()
        hashtable.set(current_node.value, True)  # Use node.value as key
        # Note: Right child is pushed first so that the left child is processed first
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

# RECURSIVE METHOD
# def tree_intersection(tree1, tree2):
#     def traverse_and_set_values(node, hashtable):
#         if not node:
#             return
#         hashtable.set(node.value, True)  # Use node.value as key; value is just a placeholder
#         traverse_and_set_values(node.left, hashtable)
#         traverse_and_set_values(node.right, hashtable)

#     def find_matches(node, hashtable, matches):
#         if not node:
#             return
#         if hashtable.has(node.value):
#             matches.add(node.value)
#         find_matches(node.left, hashtable, matches)
#         find_matches(node.right, hashtable, matches)

#     # Initialize the hashtable and matches set
#     hashtable_for_tree1 = Hashtable()
#     matches = set()

#     # Populate the hashtable with values from the first binary tree
#     traverse_and_set_values(tree1.root, hashtable_for_tree1)


#     # Traverse the second binary tree and find matches
#     find_matches(tree2.root, hashtable_for_tree1, matches)

#     return matches



