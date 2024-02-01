from data_structures.queue import Queue


class KaryTree:
    """
    Represents a K-ary tree where each node can have up to K children.

    A K-ary tree is a generalization of a binary tree, suitable for use where tree nodes
    might have more than two children. This implementation provides methods for performing
    breadth-first traversal and cloning the tree.

    Attributes:
        root (Node, optional): The root node of the tree. Defaults to None.

    Parameters:
        root (Node, optional): An optional root node from which the tree will be grown.
    """
    def __init__(self, root=None):
        """
        Initializes a new instance of a K-ary tree.

        Parameters:
            root (Node, optional): The root node of the K-ary tree. Defaults to None.
        """
        self.root = root

    def breadth_first(self):
        """
        Performs a breadth-first traversal of the tree.

        Starts from the root and explores all nodes at the present depth prior to moving on to the nodes
        at the next depth level. This method uses a queue to keep track of the order in which to explore nodes.

        Returns:
            list: A collection of node values in the order they were visited during the traversal.
        """
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone(self):
        """
        Creates a deep copy of the tree.

        Recursively traverses the original tree, starting from the root, to create a new tree with the same structure
        and values but with entirely new node instances.

        Returns:
            KaryTree: A new instance of KaryTree, which is a clone of the original tree.
        """

        def traverse(source_node):
            """
            Recursively clones a subtree starting from the given node.

            Parameters:
                source_node (Node): The node to start cloning from.

            Returns:
                Node: The root node of the cloned subtree. Returns None if source_node is None.
            """
            if source_node is None:
                return

            clone_node = Node(source_node.value)

            for source_child in source_node.children:
                cloned_child = traverse(source_child)
                if cloned_child:
                    clone_node.children.append(cloned_child)

            return clone_node

        cloned_tree = KaryTree()
        cloned_tree.root = traverse(self.root)

        return cloned_tree


class Node:
    """
    K-Ary Tree Node
    The number of children nodes is not restricted
    """

    def __init__(self, value):
        self.value = value
        self.children = []
