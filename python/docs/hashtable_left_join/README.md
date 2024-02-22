# HashTable Left Join
<!-- Description of the challenge -->

Write a function called left join

- Arguments: two hash maps
  - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
  - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

Notes:

- Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
- LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
- If no values exist in the right hashmap, then some flavor of `NULL` should be appended to the result row.

## Examples

### INPUT

Synonyms / Antonyms

| Key | Value |  | Key | Value |
| ---- | ---- | ---- | ---- | ---- |
| diligent | employed |  | diligent | idle |
| fond | enamored |  | fond | averse |
| guide | usher |  | guide | follow |
| outfit | garb |  | flow | jam |
| wrath | anger |  | wrath | delight |

### OUTPUT

```python
[
   ["fond", "enamored", "averse"],
   ["wrath", "anger", "delight"],
   ["diligent", "employed", "idle"],
   ["outfit", "garb", "NONE"],
   ["guide", "usher","follow"]
]
```

## Whiteboard Process

![Left Join Whiteboard](hashtable_left_join_whiteboard.png)

## Approach & Efficiency

### Space Complexity

O(n) where n is the number of keys in synonyms hashtable

### Time Complexity

O(n) where n is the number of keys in the synonyms hashtable

## Tests

`pytest -k test_hashtable_left_join.py`

## Run Code

`python3 -m code_challenges.hashtable_left_join`

## Solution

[hashtable_left_join.py](../../code_challenges/hashtable_left_join.py)
