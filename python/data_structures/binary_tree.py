class BinaryTree:
    """
    Defines Binary Tree class.

    Depth first traversal methods:
    pre-order
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
              a
          b      c
        d  e    f  g

        ["a",       "b", "d", "e",      "c", "f", "g"]

        root -> left -> right
        BUT "root" depends on context
        It's not necessarily same as root of overall tree

        """

        def depth_first_values(root):
            """
            return my result + left node's result + right node's result

            ["a"] + ["b","d","e"] + ["c","f","g"]

            return List

            """

            if root is None: # base case - check if stack is empty
                return []

            root_result = [root.value]   # ["a"]
            left_result = depth_first_values(root.left) # collect left side of tree ["b","d","e"]
            right_result = depth_first_values(root.right)# collect right side of tree ["c","f","g"]

            # ["a"] + ["b","d","e"] + ["c","f","g"]
            return root_result + left_result + right_result


        return depth_first_values(self.root)

    def in_order(self):
        """
        left -> root -> right
        traverse left, visit "root" node, visit right
        """

        def depth_first_values(root):
            """
            return left node's result + my result + right node's result
            ["b","d","e"] + ["a"] + ["c","f","g"]
            return List
            """

            if root is None:
                return []

            left_result = depth_first_values(root.left) # collect left side of tree ["b","d","e"]
            my_result = [root.value]   # ["a"]
            right_result = depth_first_values(root.right)# collect right side of tree ["c","f","g"]

            # ["b","d","e"] + ["a"] + ["c","f","g"]
            return left_result + my_result + right_result


        return depth_first_values(self.root)

    def post_order(self):
        """
        left -> right -> root
        BUT "root" depends on context
        It's not necessarily same as root of overall tree
        """

        def depth_first_values(root):
            if root is None:
                return []

            left_result = depth_first_values(root.left) # collect left sub-tree ["b","d","e"]
            right_result = depth_first_values(root.right) # collect right sub-tree ["c","f","g"]
            my_result = [root.value]   # ["a"]


            return left_result + right_result + my_result


        return depth_first_values(self.root)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
