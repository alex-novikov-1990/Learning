"""Tests for Deque."""

from deque import Deque


def test_deque_one_item():
    deque = Deque()

    assert deque.removeFront() is None
    assert deque.removeTail() is None
    assert deque.size() == 0

    # front -> tail
    deque.addFront(12)
    assert deque.size() == 1
    assert deque.removeTail() == 12
    assert deque.size() == 0
    assert deque.removeFront() is None
    assert deque.removeTail() is None

    # front -> front
    deque.addFront(13)
    assert deque.size() == 1
    assert deque.removeFront() == 13
    assert deque.size() == 0
    assert deque.removeFront() is None
    assert deque.removeTail() is None

    # tail -> tail
    deque.addTail(14)
    assert deque.size() == 1
    assert deque.removeTail() == 14
    assert deque.size() == 0
    assert deque.removeFront() is None
    assert deque.removeTail() is None

    # tail -> front
    deque.addTail(15)
    assert deque.size() == 1
    assert deque.removeFront() == 15
    assert deque.size() == 0
    assert deque.removeFront() is None
    assert deque.removeTail() is None

def test_deque_rotation_tail_to_front():
    deque = Deque()

    for i in range(20):
        deque.addTail(i)
    for _ in range(100):
        for i in range(20):
            assert deque.size() == 20
            assert deque.removeFront() == i
            assert deque.size() == 19
            deque.addTail(i)
            assert deque.size() == 20

    # check resize when queue.end <= queue.start
    assert deque.end <= deque.start # asume
    for i in range(20):
        assert deque.removeFront() == i
    assert deque.size() == 0

def test_deque_rotation_front_to_tail():
    deque = Deque()

    for i in range(20):
        deque.addFront(i)
    for _ in range(100):
        for i in range(20):
            assert deque.size() == 20
            assert deque.removeTail() == i
            assert deque.size() == 19
            deque.addFront(i)
            assert deque.size() == 20

    # check resize when queue.end <= queue.start
    assert deque.end <= deque.start # asume
    for i in range(20):
        assert deque.removeTail() == i
    assert deque.size() == 0

def test_degue_large_size_and_capacity():
    deque = Deque()

    for _ in range(10):
        for i in range(1000):
            deque.addTail(i)

        assert deque.size() == 1000

        for i in range(1000):
            assert deque.removeFront() == i

        assert deque.size() == 0
        assert deque.removeFront() is None

    assert deque.capacity == 16

    for _ in range(10):
        for i in range(1000):
            deque.addFront(i)

        assert deque.size() == 1000

        for i in range(1000):
            assert deque.removeTail() == i

        assert deque.size() == 0
        assert deque.removeTail() is None

    assert deque.capacity == 16

class Test:
    def func_a(self, input: int):
        print(input)

def test_Test():
    test = Test()
    test.func_a("abc")
