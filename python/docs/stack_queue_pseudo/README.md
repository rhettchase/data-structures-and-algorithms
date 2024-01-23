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
- Method Argument: `20`
- Internal State: `[5]->[10]->[15]`

## Whiteboard Process
<!-- Embedded whiteboard image -->


## Approach & Efficiency

## Tests

`pytest -k test_stack_queue_pseudo.py`

## Run Code

`python3 -m code_challenges.stack_queue_pseudo`

## Solution

[linked_list.py](../../data_structures/linked_list.py)

```python

```

