"""Palindrome checker via deque"""

from deque import Deque


def is_palindrome(text):
    deque = Deque()
    for symbol in text:
        deque.addTail(symbol)

    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False

    return True
