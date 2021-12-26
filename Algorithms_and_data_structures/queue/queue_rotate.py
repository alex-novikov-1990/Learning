"""Queue rotator"""


def rotate(queue, n):
    size = queue.size()
    n = n % size

    for _ in range(n):
        queue.enqueue(queue.dequeue())
