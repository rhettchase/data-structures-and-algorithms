class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    """
    Put docstring here
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
my_list.get_values()

print("str:", str(my_list))
print("repr:", repr(my_list))

print("target value included:", my_list.includes("banana"))

class TargetError:
    pass
