class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
        self.Last = -1

    def MakeHeap(self, a, depth):
        self.HeapArray = [0] * (2**(depth+1) - 1)
        result = True
        for key in a:
            result = self.Add(key)
        return result

    def GetMax(self):
        if self.Last == -1:
            return -1

        bubble_key = self.HeapArray[self.Last]
        self.HeapArray[self.Last] = 0 # unnecessary, but for convenience
        self.Last -= 1
        if self.Last == -1:
            return bubble_key

        result = self.HeapArray[0]
        bubble = 0
        max_bubble = int((self.Last - 1)/2)
        while bubble <= max_bubble:
            left = bubble * 2 + 1
            right = bubble * 2 + 2
            if bubble_key >= self.HeapArray[left] and \
               bubble_key >= self.HeapArray[right]:
                break

            # self.HeapArray[bubble] = bubble_key
            if self.HeapArray[left] >= self.HeapArray[right]:
                self.HeapArray[bubble] = self.HeapArray[left]
                bubble = left
            else:
                self.HeapArray[bubble] = self.HeapArray[right]
                bubble = right

        self.HeapArray[bubble] = bubble_key
        return result

    def Add(self, key):
        if (self.Last+1 == len(self.HeapArray)):
            return False

        self.Last += 1
        bubble = self.Last
        parrent = int((bubble - 1) / 2)
        while bubble > 0 and self.HeapArray[parrent] < key:
            self.HeapArray[bubble] = self.HeapArray[parrent]
            bubble = parrent
            parrent = int((bubble - 1) / 2)

        self.HeapArray[bubble] = key
        return True

