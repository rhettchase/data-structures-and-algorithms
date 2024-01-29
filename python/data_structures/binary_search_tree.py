from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    A Binary Search Tree (BST) data structure extending from a basic Binary Tree.

    This class provides methods for adding values and checking if a value is
    contained within the tree. The BST maintains the property where for each
    node, all elements in the left subtree are less than the node, and all
    elements in the right subtree are greater than or equal to the node. This
    ensures efficient searching, insertion, and deletion operations.

    Methods:
        add(value): Adds a new value to the BST.
        contains(value): Checks if a value is present in the BST.
    """

    def add(self, value):
        """
        Adds a new value to the binary search tree.

        This method encapsulates the value in a Node and inserts it into the
        tree. If the tree is empty, the new node becomes the root. Otherwise,
        it finds the correct position for the new node so that the BST property
        is maintained.

        Args:
            value: The value to be added to the tree.

        Returns:
            None. The tree is modified in-place.
        """

        # wrap value in Node
        new_node = Node(value)

        if self.root is None: # root check: check if tree is empty
            self.root = new_node # new_node becomes root
            return

        def walk(node_to_ask, node_to_add):
            """
            Look for the right spot to "sit" aka be added
            inspect each node and either
            a: "sit" next to it in correct spot
            b: move on in the correct direction
            """

            if node_to_add.value < node_to_ask.value:
                if node_to_ask.left is None:
                    node_to_ask.left = node_to_add
                else:
                    walk(node_to_ask.left, node_to_add)
            elif node_to_add.value >= node_to_ask.value: # >= value
                if node_to_ask.right is None:
                    node_to_ask.right = node_to_add
                else:
                    walk(node_to_ask.right, node_to_add)


        walk(self.root, new_node) # initiates process, starting from the root of the tree

    def contains(self, value):
        """
        Check if the binary search tree contains a given value.

        This method initiates a depth-first search from the root of the tree,
        recursively traversing the tree to find the specified value. It
        leverages the properties of the binary search tree where the left
        child node is less than the parent node, and the right child is
        equal or greater than the parent node.

        Args:
            value: The value to search for in the binary search tree.

        Returns:
            True if the value is found in the tree, False otherwise.
        """
        if self.root is None:
            return False

        def walk(node):
            """
            Recursively traverse the binary search tree in search of a given value.

            This inner function performs a depth-first search by comparing the current
            node's value with the target value and recursively exploring either the
            left or right subtree based on the comparison.

            Args:
                node: The current node being inspected in the binary search tree.

            Returns:
                True if the target value is found, False if the value is not found
                or the end of a branch is reached (node is None).
            """
            if node is None:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return walk(node.left)
            else:
                return walk(node.right)

        return walk(self.root)

