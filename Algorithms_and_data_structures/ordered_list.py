"""An example of ordered list"""

class Node:
    """Node for OrderedList"""
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    """An ordered list"""
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0

    def add(self, value):
        node = Node(value)

        # if empty
        if self.head is None:
            self.head = node
            self.tail = node
            return

        strong_order = (-1 if self.__ascending else 1)

        # fast add to the tail, if possible
        if self.compare(value, self.tail.value) != strong_order:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            return

        # fast add to the head, if possible
        if self.compare(value, self.head.value) == strong_order:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return

        # traverse to find place
        next_node = self.head.next
        while self.compare(value, next_node.value) != strong_order:
            next_node = next_node.next

        # before is not head and not tail because of "fast add" parts
        next_node.prev.next = node
        node.prev = next_node.prev
        next_node.prev = node
        node.next = next_node

    def find(self, val):
        strong_order = (-1 if self.__ascending else 1)
        if (self.head is None) or \
           (self.compare(val, self.head.value) == strong_order) or \
           (self.compare(self.tail.value, val) == strong_order):
            return None

        node = self.head
        while (node.next is not None) and \
              (self.compare(node.value, val) == strong_order):
            node = node.next

        if node.value == val:
            return node
        else:
            return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            return

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        node.next = None
        node.prev = None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        if self.head is None:
            return 0

        length = 1
        node = self.head
        while node.next is not None:
            length += 1
            node = node.next

        return length

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0
