"""An example of set."""


class PowerSet:
    """A set, based on a hash table
    with a separate-chaining collision resolver"""

    def __init__(self):
        self.__buckets = [None] * 16
        self.__size = 0

    def __hash_fun(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        return hash(value) % len(self.__buckets)

    def __put(self, value: str):
        value_hash = self.__hash_fun(value)
        bucket = self.__buckets[value_hash]
        if bucket is None:
            bucket = [value]
            self.__buckets[value_hash] = bucket
            return True
        elif value not in bucket:
            bucket.append(value)
            return True
        else:
            return False

    def __resize(self, new_buckets_size: int):
        old_buckets = self.__buckets
        self.__buckets = [None] * new_buckets_size

        for bucket in old_buckets:
            if bucket is None:
                continue

            for value in bucket:
                self.__put(value)

    def for_each(self, func):
        for bucket in self.__buckets:
            if bucket is None:
                continue

            for value in bucket:
                func(value)

    def size(self):
        return self.__size

    def put(self, value):
        if not self.__put(value):
            return

        self.__size += 1
        if self.__size > len(self.__buckets) * 0.9:
            self.__resize(len(self.__buckets) * 2)

    def get(self, value):
        value_hash = self.__hash_fun(value)
        bucket = self.__buckets[value_hash]
        return (bucket is not None) and (value in bucket)

    def remove(self, value):
        value_hash = self.__hash_fun(value)
        bucket = self.__buckets[value_hash]

        if (bucket is None) or (value not in bucket):
            return False

        bucket.remove(value)
        self.__size -= 1
        if (self.__size > 16) and \
           (self.__size < len(self.__buckets) * 0.5):
            self.__resize(max(16, int(len(self.__buckets) / 2)))

        return True

    def intersection(self, set2):
        if self.size() > set2.size():
            return set2.intersection(self)

        def put_if_in_set2(value):
            if set2.get(value):
                result.put(value)

        result = PowerSet()
        self.for_each(put_if_in_set2)
        return result

    def union(self, set2):
        result = PowerSet()

        self.for_each(result.put)
        set2.for_each(result.put)
        return result

    def difference(self, set2):
        result = PowerSet()

        def put_if_not_in_set2(value):
            if not set2.get(value):
                result.put(value)

        result = PowerSet()
        self.for_each(put_if_not_in_set2)
        return result


    def issubset(self, set2):
        result = True

        def taint_if_not_in_self(value):
            nonlocal result
            if not self.get(value):
                result = False

        set2.for_each(taint_if_not_in_self)
        return result

    # -------------------------------------------------------------------
    # Public methods from HashTable (are needed for automatic code check)
    # -------------------------------------------------------------------

    def hash_fun(self, value: str):
        return self.__hash_fun(value)

    def seek_slot(self, value: str):
        """Finds a bucket to place the value"""
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        return self.hash_fun(value)

    def find(self, value):
        """Finds a bucket with the value"""
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        value_hash = self.hash_fun(value)
        bucket = self.__buckets[value_hash]
        if (bucket is not None) and (value in self.__buckets[value_hash]):
            return value_hash
        else:
            return None
