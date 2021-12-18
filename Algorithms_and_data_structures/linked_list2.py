"""An example of doubly linked list"""

class Node:
    """A node of doubly linked list"""
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    """A doubly linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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

    def __delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        node.prev = None
        node.next = None
        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node
        if prev_node is None:
            self.head = next_node
        if next_node is None:
            self.tail = prev_node

    def delete(self, val, all=False):
        found = False
        node = self.head
        while node is not None:
            if node.value == val:
                next_node = node.next
                self.__delete_node(node)
                node = next_node

                if all:
                    found = True
                else:
                    return True
            else:
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
            afterNode = self.tail

        if afterNode is None:
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = afterNode.next
        afterNode.next = newNode
        newNode.prev = afterNode

        if newNode.next is None:
            self.tail = newNode
        else:
            newNode.next.prev = newNode

    def add_in_head(self, newNode):
        newNode.next = self.head
        self.head = newNode
        if newNode.next is None:
            self.tail = newNode
        else:
            newNode.next.prev = newNode
