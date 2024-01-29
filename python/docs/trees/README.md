# Binary Tree and Binary Search Tree Implementation
<!-- Description of the challenge -->
### Node

- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

### Binary Tree

- Create a Binary Tree class
    - Define a method for each of the depth first traversals:
        - pre order
        - in order
        - post order
    - Each depth first traversal method should return an array of values, ordered appropriately.

### Binary Search Tree

- Create a Binary Search Tree class
    - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    - Add
        - Arguments: value
        - Return: nothing
        - Adds a new node with that value in the correct location in the binary search tree.
    - Contains
        - Argument: value
        - Returns: boolean indicating whether or not the value is in the tree at least once.

## Examples

N/A

## Whiteboard Process
<!-- Embedded whiteboard image -->
N/A

## Approach & Efficiency

### Time Complexity

- pre_order, in_order, post_order: O(n) - visit each node once
- add: O(log n) best/average, O(n) worst
- contains: O(log n) best/average for balanced tree, O(n) worst

### Space Complexity

- pre_order, in_order, post_order: O(h) --> O(log n) best/average, O(n) worst
- add: O(log n) best/average (balanced tree), O(n) worst
- contains: O(h) --> O(log n) best/average, O(n) worst

## Solution

[binary_tree.py](../../data_structures/binary_tree.py)
[binary_search_tree.py](../../data_structures/binary_search_tree.py)
