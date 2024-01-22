from data_structures.linked_list import Node, LinkedList
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Stack class that has a top property. It creates an empty Stack when instantiated.
    """

    def __init__(self):
        # default empty value assigned to top when stack is created
        self.top = None

    def push(self, value):
        """
        Pushes a new value onto the top of the stack.
        """
        # create a new node
        new_node = Node(value)

        # point the new node to the current top
        new_node.next = self.top

        # reassign the self.top in the stack
        self.top = new_node

    def pop(self):
        """
        Pops the top value from teh stack and returns it
        """
        # popping from an empty list
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        # get the return value
        # Temporarily reference top
        pop_value = self.top.value

        # move the pointer which "removes" the node from the Stack
        # move top to next node
        self.top = self.top.next

        # TODO: remove temp's next
        # self.top.next = None

        # return value
        return pop_value

    def is_empty(self):
        """
        Boolean indicating whether or not the stack is empty.
        """
        if self.top is None:
            return True
        else:
            False

    def peek(self):
        """
        Returns value of the node located at the top of the stack
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        peek_value = self.top.value
        return peek_value



