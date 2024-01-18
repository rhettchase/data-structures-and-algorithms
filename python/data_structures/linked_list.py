class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    """
    Class used to represent a LinkedList

    Attributes:
    value

    Methods:
    insert
    includes
    get_values
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_values(self):
        if self.head is None:
            return "NULL"

        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.value)
            current = current.next
        print(nodes)
        return(nodes)

    def append(self, value):
        # create new node
        new_node = Node(value)

        # If the list is empty, set the new node as the head and return
        if self.head is None:
            self.head = new_node
            return

        # Start with the head node
        current = self.head

        # Traverse to the end of the list
        # The loop will exit with 'current' being the last node
        while current.next is not None:
            current = current.next

        # Attach the new node at the end of the list
        current.next = new_node

    def insert_before(self, target_value, new_value):
        # Check if the list is empty
        if self.head is None:
            raise TargetError("Cannot insert before in an empty list")

        # Handle the special case where the head is the target node
        if self.head.value == target_value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse the list to find the node before the target node
        current = self.head
        while current.next:
            if current.next.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

        # If the target node is not found, raise TargetError
        raise TargetError("Target value not found in the list")

    def insert_after(self, target_value, new_value):
         # Check if the list is empty
        if self.head is None:
            raise TargetError("Cannot insert after in an empty list")

        # Traverse the list to find the target node
        current = self.head
        while current:
            # If the target node is found, insert the new node after it
            if current.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        # If the target node is not found, raise TargetError
        raise TargetError("Target value not found in the list")

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def kth_from_end(self, k):
        if self.head is None:
            raise TargetError("Empty list")

        # Check if k is negative
        if k < 0:
            raise TargetError("k must be a non-negative integer")

        # Use get_length to determine the length of the list
        length = self.get_length()
        print(length)

        # Check if k is larger than or equal to the length of the list
        if k >= length:
            raise TargetError("k is larger than the length of the list")

        # Find the (length-k-1)th node from the start
        target_index = length - 1 - k
        current = self.head
        for i in range(target_index):
            current = current.next

        return current.value





    def __str__(self):
        if self.head is None:
            return "NULL"

        current = self.head # start from first actual element
        nodes_str = []
        str_formatted = ""

        while current is not None:
            node_str = f"{{ {current.value} }}"
            nodes_str.append(node_str)
            current = current.next
        str_formatted = " -> ".join(nodes_str) + " -> NULL"
        return str_formatted

    def __repr__(self):
        current = self.head
        nodes = []

        while current is not None:
            nodes.append(str(current.value))
            current = current.next
        nodes.append("NULL")
        return " -> ".join(nodes)



my_list = LinkedList()
my_list.insert("apple")
my_list.insert("banana")
my_list.insert("cucumbers")
print(my_list.kth_from_end(0))


print("str:", str(my_list))
print("repr:", repr(my_list))

# print("target value included:", my_list.includes("banana"))

class TargetError(Exception):
    pass
