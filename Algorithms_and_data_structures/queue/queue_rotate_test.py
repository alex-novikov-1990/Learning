"""Tests for queue rotator."""


from queue import Queue
from queue_rotate import rotate

def test_rotate():
    queue1 = Queue()
    queue2 = Queue()

    for i in range(20):
        queue1.enqueue(i)
        queue2.enqueue(i)

    rotate(queue1, 77)
    for i in range(77):
        queue2.enqueue(queue2.dequeue())

    for _ in range(20):
        assert queue1.dequeue() == queue2.dequeue()
