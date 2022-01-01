"""An example of bloom filter"""

class BloomFilter:
    """A bloom filter with an integer number used as a bit storage"""

    def __init__(self, f_len):
        if (f_len > 32):
            raise ValueError("Filter length larger than 32 is not supported")

        self.filter_len = f_len
        self.data = 0b0

    def hash1(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result*17 + code) % self.filter_len

        return result

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result*223 + code) % self.filter_len

        return result

    def add(self, str1):
        self.data = self.data | (0b1 << self.hash1(str1))
        self.data = self.data | (0b1 << self.hash2(str1))

    def is_value(self, str1):
        return \
            ((self.data & (0b1 << self.hash1(str1))) != 0) and \
            ((self.data & (0b1 << self.hash2(str1))) != 0)
