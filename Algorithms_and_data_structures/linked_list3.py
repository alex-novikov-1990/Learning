"""An example of doubly linked list with a dummy nodes"""


class Node:
    """A node of doubly linked list with a dummy nodes

    To make it fully interchangable with a simple doubly linked list,
    there is a prev and next properties to hide dummy nodes"""
    def __init__(self, value):
        self.value = value
        # prev_raw and next_raw should be protected but pylint doesn't have
        # a friendship support: https://github.com/PyCQA/pylint/issues/4362
        self.prev_raw = None
        self.next_raw = None

    @property
    def prev(self):
        # isinstance(self.prev_raw, DummyNode) doesn't work here
        if hasattr(self.prev_raw, 'dummy_marker'):
            return None
        return self.prev_raw

    @prev.setter
    def prev(self, value):
        self.prev_raw = value

    @property
    def next(self):
        # isinstance(self.next_raw, DummyNode) doesn't work here
        if hasattr(self.next_raw, 'dummy_marker'):
            return None
        return self.next_raw

    @next.setter
    def next(self, value):
        self.next_raw = value

class DummyNode(Node):
    """A dummy node"""

    def __init__(self):
        Node.__init__(self, None)
        self.dummy_marker = None

class LinkedList3:
    """A doubly linked list"""
    def __init__(self):
        self._head = DummyNode()
        self._tail = DummyNode()
        self._head.next_raw = self._tail
        self._tail.prev_raw = self._head

    @property
    def head(self):
        return self._head.next

    @property
    def tail(self):
        return self._tail.prev

    def add_in_tail(self, item):
        item.prev_raw = self._tail.prev_raw
        item.next_raw = self._tail
        item.prev_raw.next_raw = item
        self._tail.prev_raw = item

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
        prev_node = node.prev_raw
        next_node = node.next_raw
        prev_node.next_raw = next_node
        next_node.prev_raw = prev_node
        node.prev_raw = None
        node.next_raw = None

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
        self.__init__()

    def len(self):
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next

        return i

    def insert(self, afterNode, newNode):
        if afterNode is None:
            afterNode = self._tail.prev_raw

        newNode.next_raw = afterNode.next_raw
        newNode.prev_raw = afterNode
        afterNode.next_raw = newNode
        newNode.next_raw.prev_raw = newNode

    def add_in_head(self, newNode):
        newNode.next_raw = self._head.next_raw
        newNode.prev_raw = self._head
        self._head.next_raw = newNode
        newNode.next_raw.prev_raw = newNode
