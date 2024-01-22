# Stack and Queue Implementation
<!-- Description of the challenge -->

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue.

## `Stack`

- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- This object should be aware of a default empty value assigned to top when the stack is created.
- The class should contain the following methods:

`push`

- Arguments: value
- adds a new node with that value to the top of the stack with an O(1) Time performance.

`pop`

- Arguments: none
- Returns: the value from node from the top of the stack
- Removes the node from the top of the stack
- Should raise exception when called on empty stack

`peek`

- Arguments: none
- Returns: Value of the node located at the top of the stack
- Should raise exception when called on empty stack

`is empty`

- Arguments: none
- Returns: Boolean indicating whether or not the stack is empty.

## `Queue`

- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
- This object should be aware of a default empty value assigned to front when the queue is created.
- The class should contain the following methods:

`enqueue`

- Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

`dequeue`

- Arguments: none
- Returns: the value from node from the front of the queue
- Removes the node from the front of the queue
- Should raise exception when called on empty queue

`peek`

- Arguments: none
- Returns: Value of the node located at the front of the queue
- Should raise exception when called on empty stack

`is empty`

- Arguments: none
- Returns: Boolean indicating whether or not the queue is empty

## Examples

N/A

## Whiteboard Process
<!-- Embedded whiteboard image -->
N/A

## Approach & Efficiency

For the Stack class, the `push`, `pop`, `peek`, and `is_empty` methods all have time efficiency of O(1)

For the Queue class, the `enqueue`, `dequeue`, `peek`, and `is_empty` methods all have time efficiency of O(1)

## Tests

- `pytest -k test_stack.py`
- `pytest -k test_queue.py`

## Run Code

- `python3 -m data_structures.stack`
- `python3 -m data_structures.queue`

## Solution

- [stack.py](../../data_structures/stack.py)
- [queue.py](../../data_structures/queue.py)

```python
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
            False
```
