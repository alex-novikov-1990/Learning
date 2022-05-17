"""Tests for double-stack queue."""

from double_stack_queue import Queue


def test_queue():
    queue = Queue()

    assert queue.dequeue() is None
    assert queue.size() == 0

    queue.enqueue(12)
    assert queue.size() == 1
    assert queue.dequeue() == 12
    assert queue.size() == 0
    assert queue.dequeue() is None

    # check start+end rotation
    for i in range(20):
        queue.enqueue(i)
    for _ in range(100):
        for i in range(20):
            assert queue.size() == 20
            assert queue.dequeue() == i
            assert queue.size() == 19
            queue.enqueue(i)
            assert queue.size() == 20

    for i in range(20):
        assert queue.dequeue() == i
    assert queue.size() == 0

    # check large volume
    for _ in range(10):
        for i in range(1000):
            queue.enqueue(i)

        assert queue.size() == 1000

        for i in range(1000):
            assert queue.dequeue() == i

        assert queue.size() == 0
        assert queue.dequeue() is None
