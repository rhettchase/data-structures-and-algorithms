# HashTable Implementation
<!-- Description of the challenge -->

Implement a Hashtable Class with the following methods:

`set`
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.

- Arguments: key, value
- Returns: nothing

`get`

- Arguments: key
- Returns: Value associated with that key in the table

`has`

- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.

`keys`

- Returns: Collection of keys

`hash`

- Arguments: key
- Returns: Index in the collection for that key

## Examples

See tests

## Whiteboard Process

N/A

## Approach & Efficiency

### Space Complexity

O(n + m): The space complexity is linear with respect to the number of key-value pairs (n) and size of array (m).

### Time Complexity

- Best case: The efficiency of hash table operations is generally O(1), assuming a good hash function and load factor.
- Worst case: due to the use of chaining, operations can degrade to O(n), where n is the number of entries in a single bucket.
- Fetching all keys (keys): O(n + m).
  - This operation involves traversing all buckets and the linked lists within them. Every key is visited once, but every bucket is also examined, making the time complexity linear with respect to both the number of keys and the number of buckets.

## Tests

`pytest -k test_hashtable.py`

## Run Code

`python3 -m data_structures.hashtable`

## Solution

[hashtable.py](../../data_structures/hashtable.py)
