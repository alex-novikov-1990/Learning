"""A simple example of linked list"""

class Node:
    """A node of LinkedList"""

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    """A linked list"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        found = False

        # process nodes at the head
        while self.head is not None and self.head.value == val:
            node = self.head
            self.head = node.next
            node.next = None
            if self.head is None:
                self.tail = None

            if all:
                found = True
            else:
                return True

        if self.head is None:
            return found

        # process nodes after the head
        prev = self.head
        node = prev.next
        while node is not None:
            if node.value == val:
                prev.next = node.next
                node.next = None
                node = prev.next
                if node is None:
                    self.tail = prev

                if all:
                    found = True
                else:
                    return True
            else:
                prev = node
                node = node.next

        return found


    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next

        return i

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

        if newNode.next is None:
            self.tail = newNode
