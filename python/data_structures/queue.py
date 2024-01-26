from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Queue class that has a front property. It creates an empty Queue when instantiated.
    """
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        """
        Adds a new node to the end of the queue, with the provided value.
        """
        new_node = Node(value)

        # if the Queue is empty
        if self.is_empty():
           self.front = new_node
           self.back = new_node
        else:
            # Queue isn't empty
            self.back.next = new_node
            # point the queue's self.back to our new node. Update the pointer!
            self.back = new_node

    def dequeue(self):
        """
        Removes the front node from the queue and returns its value.
        """
        # if the Queue is empty
        if self.front is None:
            raise InvalidOperationError("Cannot dequeue from empty queue")

        # get the value
        dequeue_value = self.front.value

        # move the front pointer to its next
        self.front = self.front.next

        # the Queue has become empty
        if self.front is None:
            # also need to update self.back
            self.back = None

        return dequeue_value

    def peek(self):
        """
        Inspects front of the queue and returns value of the node located at the front of the queue
        """
        # if the Queue is empty
        if self.is_empty():
            raise InvalidOperationError("Cannot peek at value of empty queue")
        peek_value = self.front.value
        return peek_value

        pass

    def is_empty(self):
        """
        Boolean indicating whether or not the queue is empty.
        """
        if self.front is None:
            return True
        else:
            return False
