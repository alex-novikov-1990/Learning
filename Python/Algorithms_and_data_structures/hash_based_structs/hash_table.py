"""An example of hash table"""


class HashTable:
    """A hash table with a linear probing"""

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        return hash(value) % self.size

    def seek_slot(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        start = self.hash_fun(value)
        if self.slots[start] is None \
           or (self.slots[start] == value):
            return start

        current = (start + self.step) % self.size
        while current != start:
            if (self.slots[current] is None) \
                or (self.slots[current] == value):
                return current

            current = (current + self.step) % self.size

        return None

    def put(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        slot = self.seek_slot(value)
        if slot is None:
            return None

        self.slots[slot] = value
        return slot

    def find(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        start = self.hash_fun(value)
        if self.slots[start] == value:
            return start

        current = (start + self.step) % self.size
        while current != start:
            if self.slots[current] == value:
                return current

            current = (current + self.step) % self.size

        return None
