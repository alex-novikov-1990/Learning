"""An example of cache."""

class NativeCache:
    """A cache, which is based on a fixed size dictionary
    and uses cache hits counters to choose an element to
    overwrite on cache overflow."""

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")

        return hash(key) % self.size

    def __find_slot(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")

        start_slot = self.hash_fun(key)
        if self.slots[start_slot] is None \
           or (self.slots[start_slot] == key):
            return (start_slot, None)

        min_hits = self.hits[start_slot]
        min_hits_slot = start_slot
        current_slot = (start_slot + 1) % self.size
        while current_slot != start_slot:
            if (self.slots[current_slot] is None) \
                or (self.slots[current_slot] == key):
                return (current_slot, None)

            if self.hits[current_slot] < min_hits:
                min_hits = self.hits[current_slot]
                min_hits_slot = current_slot

            current_slot = (current_slot + 1) % self.size

        return (None, min_hits_slot)


    def is_key(self, key):
        """Note that this method calls don't increase hits counters."""
        # it was tough decision whether to count is_key towards cache hits,
        # and the main reasoning behind not counting is that the
        # `if is_key(key) than get(key)` idiom should be counted as one hit.
        slot, _ = self.__find_slot(key)
        return (slot is not None) and (self.slots[slot] == key)

    def put(self, key, value):
        slot, min_hits_slot = self.__find_slot(key)

        if slot is not None:
            self.slots[slot] = key
            self.values[slot] = value
        else:
            self.slots[min_hits_slot] = key
            self.values[min_hits_slot] = value
            self.hits[min_hits_slot] = 0

    def get(self, key):
        slot, _ = self.__find_slot(key)
        if (slot is None) or (self.slots[slot] != key):
            return None

        self.hits[slot] += 1
        return self.values[slot]
