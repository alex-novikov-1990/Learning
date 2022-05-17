"""Tests for Heap."""

from random import randint
from heap import Heap


def test_heap():
    heap = Heap()

    heap.MakeHeap([], 0)
    assert len(heap.HeapArray) == 1
    assert heap.GetMax() == -1
    assert heap.Add(15)
    assert heap.GetMax() == 15
    assert heap.GetMax() == -1

    depth = randint(0, 10)
    size = 2**(depth+1) - 1
    values = [randint(0, size) for _ in range(randint(0, size))]
    heap.MakeHeap(values, depth)
    assert len(heap.HeapArray) == size

    for _ in range(100):
        values = sorted(values)
        for _ in range(randint(0, size)):
            assert heap.GetMax() == (values.pop() if len(values) > 0 else -1)
            assert heap.HeapArray[len(values):] == [0] * (size - len(values))
        for _ in range(randint(0, size)):
            new_value = randint(0, size)
            if len(values) < size:
                values.append(new_value)
                assert heap.Add(new_value)
            else:
                assert not heap.Add(new_value)
            assert heap.HeapArray[len(values):] == [0] * (size - len(values))

    values = sorted(values)
    while len(values) > 0:
        assert heap.GetMax() == values.pop()
        assert heap.HeapArray[len(values):] == [0] * (size - len(values))

    assert heap.GetMax() == -1
