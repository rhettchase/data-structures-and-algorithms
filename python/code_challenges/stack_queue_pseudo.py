from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError


class PseudoQueue:
    """
    Class uses 2 stacks to implement a queue's standard interface (the methods enqueue and dequeue).
    """
    def __init__(self):
        """
        Instantiate a new PseudoQueue that internally uses 2 stacks.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Inserts a value into the PseudoQueue, using a first-in, first-out approach.
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        Extracts a value from the PsuedoQueue, using a first-in, first-out approach.

        Should raise exception when called on empty queue.
        """
        stack1 = self.stack1
        stack2 = self.stack2
        if stack2.is_empty():
            if stack1.is_empty():
                raise InvalidOperationError("Queue is empty")
            while not stack1.is_empty():
                top = stack1.pop()
                stack2.push(top)
        return stack2.pop()

