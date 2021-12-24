"""Queue rotator"""


def rotate(queue, n):
    size = queue.size()
    while n > size:
        n -= size

    for _ in range(n):
        queue.enqueue(queue.dequeue())
