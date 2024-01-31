from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    """
    Function that performs breadth-first traversal of the tree

    - Arguments: tree
    - Return: list of all values in the tree, in the order they were encountered
    """
    if tree.root is None:
        return []

    queue = Queue()
    queue.enqueue(tree.root)
    values = []

    while not queue.is_empty():
        current = queue.dequeue()
        values.append(current.value)

        if current.left is not None:
            queue.enqueue(current.left)

        if current.right is not None:
            queue.enqueue(current.right)

    return values
