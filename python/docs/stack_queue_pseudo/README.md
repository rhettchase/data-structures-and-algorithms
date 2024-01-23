# Linked List kth From End
<!-- Description of the challenge -->
Create a new class called pseudo queue without using an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below). Internally, utilize 2 Stack instances to create and manage the queue

Methods:

`enqueue`

- Arguments: value
- Inserts a value into the PseudoQueue, using a first-in, first-out approach.

`dequeue`

- Arguments: none
- Extracts a value from the PseudoQueue, using a first-in, first-out approach.

NOTE: The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Examples

`enqueue(value)`

- Input: `[10]->[15]->[20]`
- Method Argument: `5`
- Internal State: `[5]->[10]->[15]->[20]`

`dequeue()`

- Input: `[5]->[10]->[15]->[20]`
- Output: `20`
- Internal State: `[5]->[10]->[15]`

## Whiteboard Process
<!-- Embedded whiteboard image -->


## Approach & Efficiency

- Enqueue: O(1) - Constant time complexity.
- Dequeue: O(n) in the worst case (when transferring elements), but O(1) amortized over a large number of operations.
  - When stack2 is empty, you need to transfer all the elements from stack1 to stack2. This transfer involves popping each element from stack1 and pushing it onto stack2. If there are n elements in stack1, this operation takes O(n) time, where n is the number of elements being transferred.

## Tests

`pytest -k test_stack_queue_pseudo.py`

## Run Code

`python3 -m code_challenges.stack_queue_pseudo`

## Solution

[stack_queue_pseudo.py](../../code_challenges/stack_queue_pseudo.py)

```python
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
```
