"""A double ended queue example"""


class Deque:
    """A double ended queue based on Python list"""

    def __init__(self):
        self.start = 0
        self.end = None
        self.data = [None] * 16
        self.capacity = 16

    def ensure_capacity(self, capacity: int):
        size = self.size()
        if size > capacity:
            raise ValueError(
                f"Target capacity ({capacity}) is less " +
                f"than a size ({size}) of queue")

        # (ctypes.py_object * capacity)() if 'import ctypes' is allowed
        new_data = [None] * capacity
        if self.end <= self.start:
            for i in range(self.start, self.capacity):
                new_data[i - self.start] = self.data[i]
            for i in range(self.end):
                new_data[i + self.capacity - self.start] = self.data[i]
        else:
            for i in range(self.start, self.end):
                new_data[i - self.start] = self.data[i]

        self.start = 0
        self.end = size if size != 0 else None
        self.capacity = capacity
        self.data = new_data

    def addFront(self, item):
        if self.size() >= self.capacity:
            self.ensure_capacity(self.capacity * 2)

        if self.end is None:
            self.end = self.start

        self.start -= 1
        if self.start < 0:
            self.start = self.capacity - 1

        self.data[self.start] = item

    def addTail(self, item):
        if self.size() >= self.capacity:
            self.ensure_capacity(self.capacity * 2)

        if self.end is None:
            self.end = self.start + 1
        else:
            self.end += 1

        self.data[self.end-1] = item

        if self.end >= self.capacity:
            self.end = 0

    def removeFront(self):
        size = self.size()
        if size == 0:
            return None

        result = self.data[self.start]
        if size == 1:
            self.end = None
            self.start = 0
            return result

        self.start += 1
        if self.start >= self.capacity:
            self.start = 0

        if ((self.size()*2) < self.capacity) and (self.capacity > 16):
            self.ensure_capacity(max(int(self.capacity / 2), 16))

        return result

    def removeTail(self):
        size = self.size()
        if size == 0:
            return None

        if size == 1:
            result = self.data[self.start]
            self.end = None
            self.start = 0
            return result

        result = self.data[self.end - 1 if self.end > 0 else self.capacity - 1]

        self.end -= 1
        if self.end < 0:
            self.end = self.capacity - 1

        if ((self.size()*2) < self.capacity) and (self.capacity > 16):
            self.ensure_capacity(max(int(self.capacity / 2), 16))

        return result

    def size(self):
        if self.end is None:
            return 0

        if self.end <= self.start:
            return self.capacity - self.start + self.end

        return self.end - self.start
