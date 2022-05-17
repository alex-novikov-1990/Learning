"""A module with a stack based on a reversed list"""

class Stack:
    """A stack as a thin wrapper around the native Python list,
    but with use of list head as a top of the stack
    (it is slow, don't use it)"""

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop(0)

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if len(self.stack) == 0:
            return None

        return self.stack[0]
