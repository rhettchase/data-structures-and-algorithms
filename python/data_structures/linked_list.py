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

    def insert_before(self, value, new_value):
        # create new node
        new_node = Node(new_value)

        # If the list is empty, raise TargetError
        if self.head is None:
            raise TargetError("Cannot insert before in an empty list")

        # If the head is the target node, insert the new node before head
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

         # Traverse the list to find the node before the target node
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        # If the target node is found, insert the new node before it
        if current.next is not None:
            new_node.next = current.next
            current.next = new_node
        # If the target node is not found, return the list as is
        else:
            # If the target node is not found, raise TargetError
            raise TargetError("Target value not found in the list")

    def __str__(self):
        if self.head is None:
            return "NULL"

        current = self.head # start from first actual element
        nodes_str = []
        str_formatted = ""

        while current is not None:
            node_str = f"{{ {current.value} }}"
            nodes_str.append(node_str)
            print(nodes_str)
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
my_list.insert_before("apple", "cucumber")
# my_list.get_values()

print("str:", str(my_list))
print("repr:", repr(my_list))

# print("target value included:", my_list.includes("banana"))

class TargetError(Exception):
    pass
