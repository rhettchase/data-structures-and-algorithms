class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = Node()

    def insert(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def display(self):
        elems = []
        current = self.head
        while current.next != None:
            current = current.next
            elems.append(current.data)
        print(elems)


    def __str__(self):

        current = self.head

        string_representation = ""

        while current:
            formatted_current_value = f"{{ {current.value} }} -> " # two brackets required in f string to become the literal curly bracket
            string_representation += formatted_current_value
            current = current.next

        string_representation += "NULL"

        return string_representation
    

my_list = LinkedList()
my_list.insert("apple")
my_list.insert("banana")
my_list.display()

class TargetError:
    pass
