from data_structures.linked_list import LinkedList


class Hashtable:
    """
    A hash table implementation that uses chaining for collision resolution. Internally, it uses a list of linked lists (buckets) to store key-value pairs.

    Attributes:
        _size (int): The size of the hash table's array. Determines the number of buckets.
        _buckets (list): A list of buckets, where each bucket is a linked list to handle collisions.

    Methods:
        __init__(self, size=1024): Initializes a new hash table with a specified size.
        set(self, key, value): Inserts or updates a key-value pair in the hash table.
        get(self, key): Retrieves the value associated with a given key from the hash table.
        has(self, key): Checks if a given key exists in the hash table.
        keys(self): Returns a list of all keys present in the hash table.
        _hash(self, key): Hashes a key to an index in the hash table.
    """

    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size

    def set(self, key, value):
        """
        Inserts or updates a key-value pair in the hash table.
        - Hash the key
        - Find the bucket
        - Search for the key
        - Update the value if found

        This method hashes the given key to find the appropriate bucket for storing the key-value pair. If the bucket does not exist, it creates a new linked list at that index. It then checks the linked list for an existing entry with the same key. If such an entry is found, its value is updated with the new value provided. Otherwise, a new key-value pair is appended to the end of the linked list, effectively handling collisions through chaining.

        If a collision occurs (i.e., different keys hash to the same bucket), this method ensures that all key-value pairs within that bucket are stored in a linked list, maintaining the integrity of the hash table and allowing for efficient retrieval and updating of values.

        Arguments:
            - key: The key to insert or update in the hash table. The key should be hashable.
            - value: The value to associate with the key.

        Returns:
        None. This method does not return a value but updates the hash table in place.
        """
        index = self._hash(key) # hash the key
        bucket = self._buckets[index] # locate the bucket at that index

        if bucket is None: # if bucket is empty, create one as a linked list
            bucket = LinkedList()
            self._buckets[index] = bucket

        # look to see if there is collision, starting at head
        current = bucket.head

        while current:
            candidate_kv_pair = current.value
            if candidate_kv_pair[0] == key: # if given key already exists, set its value with new value
                candidate_kv_pair[1] = value
                return
            current = current.next # traverse to next node

        kv_pair = [key, value] # if no pre-existing key exists, add kvp to bucket
        bucket.insert(kv_pair) # insert key value pair in the table


    def get(self, key):
        """
        Arguments: key
        Returns: Value associated with that key in the table
        """
        index = self._hash(key) # hash the key
        bucket = self._buckets[index] # locate the bucket at that index

        if bucket is None: # return None if the bucket is empty
            return None

        # traverse linked list to look for the key, starting at head
        current = bucket.head

        while current: # current is node of linked list
            kv_pair = current.value
            if kv_pair[0] == key: # index 0 is the key and index 1 is the value
                return kv_pair[1]

            current = current.next # traverse to next node of linked list

        # raise KeyError("Unable to find key: ", key)
        return None

    def has(self, key):
        """
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        """
        for bucket in self._buckets: # list of buckets (linked lists)
            if bucket: # for buckets that are not empty
                # traverse through each node of linked list, starting at bucket's head
                current = bucket.head
                while current:
                    kv_pair = current.value
                    if kv_pair[0] == key:
                        return True
                    current = current.next # keep looking
        return False # if not found, return False

    def keys(self):
        """
        Collects and returns a list of all keys stored in the hash table.

        This method iterates over each bucket in the hash table, each of which may contain a linked list due to the use of chaining to handle collisions. For each linked list found, the method traverses through all its nodes, extracting the key from each key-value pair stored as the node's value. These keys are then accumulated in a list.

        Returns:
            - key_list (list): A list of all keys present in the hash table. If the hash table is empty, an empty list is returned.

        """

        key_list = []
        # go through buckets and check for keys
        for bucket in self._buckets: # list of buckets (linked lists)
            if bucket: # for buckets that are not empty
                # traverse through each node of linked list, starting at bucket's head
                current = bucket.head
                while current:
                    kv_pair = current.value # Each node in the linked list represents a key-value pair, and is stored in the value attribute of the node.
                    key_list.append(kv_pair[0]) # add the key to the collection
                    current = current.next
        return key_list


    def _hash(self, key):
        """
        Generates a hash value for the given key. The key can be an integer or a string.
        If the key is an integer, it is directly used in the hash computation.
        If the key is a string, its characters' ASCII values are summed up.
        The hash value is obtained by multiplying the sum by a prime number and taking the modulo with the array size.

        Arguments:
            key: The key to hash, can be an integer or a string.
        Returns:
            The index in the array for that key.
        """
        hash_sum = 0

        if isinstance(key, int):  # If key is an integer
            hash_sum = key
        elif isinstance(key, str):  # If key is a string
            for char in key:
                hash_sum += ord(char)
        else:
            raise TypeError("Hashtable keys must be either int or str.")

        hash_sum *= 599  # Multiply by a prime number
        index = hash_sum % self._size  # Use modulo to fit the hash value into the table size
        return index



