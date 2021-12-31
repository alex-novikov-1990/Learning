"""An example of dictionary"""


class NativeDictionary:
    """A dictionary"""

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")

        return hash(key) % self.size

    def __find_slot(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")

        start = self.hash_fun(key)
        if self.slots[start] is None \
           or (self.slots[start] == key):
            return start

        step = 1
        current = (start + step) % self.size
        while current != start:
            if (self.slots[current] is None) \
                or (self.slots[current] == key):
                return current

            current = (current + step) % self.size

        return None


    def is_key(self, key):
        slot = self.__find_slot(key)
        return (slot is not None) and (self.slots[slot] == key)

    def put(self, key, value):
        slot = self.__find_slot(key)
        if slot is None:
            raise ValueError("Dictionary is full, only overwrites are supported")

        self.slots[slot] = key
        self.values[slot] = value

    def get(self, key):
        slot = self.__find_slot(key)
        if slot is None:
            return None

        return self.values[slot]
