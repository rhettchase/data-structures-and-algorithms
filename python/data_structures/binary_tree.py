class BinaryTree:
    """
    A BinaryTree class representing a binary tree structure.

    Attributes:
        root (Node or None): The root node of the binary tree. Initially None.

    Methods:
        pre_order(): Performs a pre-order depth-first traversal of the tree.
        in_order(): Performs an in-order depth-first traversal of the tree.
        post_order(): Performs a post-order depth-first traversal of the tree.
    """

    def __init__(self):
        """Initializes an empty binary tree with the root set to None."""
        self.root = None

    def pre_order(self):
        """
        Performs a pre-order traversal of the binary tree.

        This method traverses the tree in the order of root, left, right.
        It starts at the root of the tree, then recursively visits the left
        and right subtrees.

        Returns:
            List: A list of values representing the pre-order traversal of the tree.
              a
          b      c
        d  e    f  g

        ["a",       "b", "d", "e",      "c", "f", "g"]

        root -> left -> right
        BUT "root" depends on context
        It's not necessarily same as root of overall tree

        """

        def traverse(root):
            """
            Helper function to perform pre-order traversal from a given node.

            Args:
                root (Node): The root node from which to start the traversal.

            Returns:
                List: A list of values obtained from pre-order traversal.
            """

            if root is None: # base case - check if stack is empty
                return []

            root_result = [root.value]   # ["a"]
            left_result = traverse(root.left) # collect left side of tree ["b","d","e"]
            right_result = traverse(root.right)# collect right side of tree ["c","f","g"]

            # ["a"] + ["b","d","e"] + ["c","f","g"]
            return root_result + left_result + right_result


        return traverse(self.root)

    def in_order(self):
        """
        Performs an in-order traversal of the binary tree.

        This method traverses the tree in the order of left, root, right.
        It starts with the leftmost node, then visits the root and right subtree.

        Returns:
            List: A list of values representing the in-order traversal of the tree.
        left -> root -> right
        traverse left, visit "root" node, visit right
        """

        def traverse(root):
            """
            Helper function to perform in-order traversal from a given node.

            Args:
                root (Node): The root node from which to start the traversal.

            Returns:
                List: A list of values obtained from in-order traversal.

            return left node's result + my result + right node's result
            ["b","d","e"] + ["a"] + ["c","f","g"]
            return List
            """

            if root is None:
                return []

            left_result = traverse(root.left) # collect left side of tree ["b","d","e"]
            my_result = [root.value]   # ["a"]
            right_result = traverse(root.right)# collect right side of tree ["c","f","g"]

            # ["b","d","e"] + ["a"] + ["c","f","g"]
            return left_result + my_result + right_result


        return traverse(self.root)

    def post_order(self):
        """
        Performs a post-order traversal of the binary tree.

        This method traverses the tree in the order of left, right, root.
        It starts with the left subtree, then right subtree, and finally the root node.

        Returns:
            List: A list of values representing the post-order traversal of the tree.
        left -> right -> root
        BUT "root" depends on context
        It's not necessarily same as root of overall tree
        """

        def traverse(root):
            """
            Helper function to perform post-order traversal from a given node.

            Args:
                root (Node): The root node from which to start the traversal.

            Returns:
                List: A list of values obtained from post-order traversal.
            """
            if root is None:
                return []

            left_result = traverse(root.left) # collect left sub-tree ["b","d","e"]
            right_result = traverse(root.right) # collect right sub-tree ["c","f","g"]
            my_result = [root.value]   # ["a"]


            return left_result + right_result + my_result


        return traverse(self.root)

class Node:
    """
    A Node class for the elements of a BinaryTree.

    Attributes:
        value: The value stored in the node.
        left (Node or None): The left child of the node. Initially None.
        right (Node or None): The right child of the node. Initially None.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
