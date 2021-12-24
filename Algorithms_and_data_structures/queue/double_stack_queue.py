"""A queue example"""


class Queue:
    """A queue based on Python list"""

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def enqueue(self, item):
        self.inputStack.append(item)

    def dequeue(self):
        if len(self.outputStack) > 0:
            return self.outputStack.pop()

        if len(self.inputStack) == 0:
            return None

        while len(self.inputStack) > 1:
            self.outputStack.append(self.inputStack.pop())

        return self.inputStack.pop()

    def size(self):
        return len(self.outputStack) + len(self.inputStack)
