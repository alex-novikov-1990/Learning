"""A module with a stack example"""

class Stack:
    """A stack as a thin wrapper around the native Python list"""

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return None

        return self.stack[-1]
