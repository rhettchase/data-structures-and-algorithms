from data_structures.linked_list import Node, LinkedList


def zip_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    new_head = Node() # dummy node to start new list
    current = new_head

    pointer1 = list1.head
    pointer2 = list2.head

    while pointer1 and pointer2:
        # attach one node from list1
        current.next = pointer1
        pointer1 = pointer1.next
        current = current.next

        # attach one node from list2
        current.next = pointer2
        pointer2 = pointer2.next
        current = current.next

        # if one of the lists is not yet exhausted, attach the remaining nodes

    if pointer1:
        current.next = pointer1
    elif pointer2:
        current.next = pointer2

    # Create a new LinkedList object with the new_head.next as the head
    zipped_list = LinkedList()
    zipped_list.head = new_head.next
    return zipped_list

linked_list_a = LinkedList()
linked_list_a.insert(3)
linked_list_a.insert(2)
linked_list_a.insert(1)

linked_list_b = LinkedList()
linked_list_b.insert("c")
linked_list_b.insert("b")
linked_list_b.insert("a")

print(zip_lists(linked_list_a, linked_list_b))
