# Linked List Insertions
<!-- Description of the challenge -->
Add the following methods to the LinkedList class: `append`, `insert before`, `insert after`

`append`

- arguments: new value
- adds a new node with the given value to the end of the list

`insert before`

- arguments: value, new value
- adds a new node with the given new value immediately before the first node that has the value specified

`insert after`

- arguments: value, new value
- adds a new node with the given new value immediately after the first node that has the value specified

## Examples

### `Append`

- Initial List: `head -> {1} -> {3} -> {2} -> X`
- Method Argument: `5`
- Resulting List: `head -> {1} -> {3} -> {2} -> {5} -> X`

- Initial List: `head -> X`
- Method Argument: `1`
- Resulting List: `head -> {1} -> X`

### `Insert Before`

- Initial List: `head -> {1} -> {3} -> {2} -> X`
- Method Argument: `3, 5`
- Resulting List: `head -> {1} -> {5} -> {3} -> {2} -> X`

- Initial List: `head -> {1} -> {3} -> {2} -> X`
- Method Argument: `4, 5`
- Resulting List: `No change, method exception`

### `Insert After`

- Initial List: `head -> {1} -> {3} -> {2} -> X`
- Method Argument: `3, 5`
- Resulting List: `head -> {1} -> {3} -> {5} -> {2} -> X`

- Initial List: `head -> {1} -> {3} -> {2} -> X`
- Method Argument: `4, 5`
- Resulting List: `No change, method exception`

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Linked List Whiteboard](./Linked_List_Implementation_Whiteboard.png)

## Approach & Efficiency

I created a Node class to serve as blueprint for new node creation. I then created a LinkedList class that would create an empty linked list upon instantiation. Adding the `insert` method involved creating new instance of Node class with given value, and setting next to the head to link it to the end of the linked list. This method adds a new node with that value to the `head` of the list with an O(1) Time performance, since it will always take the same number of steps.

## Solution

[linked_list.py](../../data_structures/linked_list.py)

```python

```
