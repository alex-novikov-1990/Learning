"""An example of array-based binary search tree"""

class aBST:
    """The array-based binary search tree"""
    def __init__(self, depth):
        tree_size = 2**(depth+1) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        index = 0
        while index < len(self.Tree):
            if self.Tree[index] is None:
                return -index
            if self.Tree[index] == key:
                return index
            index = 2 * index + (2 if key > self.Tree[index] else 1)

        return None

    def AddKey(self, key):
        index = 0
        while index < len(self.Tree):
            if self.Tree[index] is None:
                self.Tree[index] = key
                return index
            if self.Tree[index] == key:
                return index
            index = 2 * index + (2 if key > self.Tree[index] else 1)

        return -1
