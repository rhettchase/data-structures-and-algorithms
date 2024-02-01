from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def fizz_buzz_tree(original_tree):
    if original_tree.root is None:
        return original_tree
    new_tree = original_tree.clone()

    def modify_nodes(node):
        if node is None: # base case
            return

        # apply FizzBuzz logic to node's value
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for child in node.children:
            modify_nodes(child) # recursively modify child nodes

    modify_nodes(new_tree.root) # start modification from root of new tree
    return new_tree





