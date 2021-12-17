"""An example of function operating on two linked lists"""

from linked_list import LinkedList, Node


def add_linked_lists(left, right):
    # If we are tight on memory, we'll probably try to add in-place
    # So we are going to build the result right away
    # and drop it if we don't need it
    result = LinkedList()
    left_node = left.head
    right_node = right.head
    while left_node is not None and right_node is not None:
        result.add_in_tail(Node(left_node.value + right_node.value))
        left_node = left_node.next
        right_node = right_node.next

    if left_node is None and right_node is None:
        return result

    return None
