"""Tests for Stack."""

from stack import Stack


def test_stack():
    stack = Stack()

    assert stack.size() == 0
    assert stack.peek() is None
    assert stack.pop() is None
    assert stack.size() == 0

    stack.push(13)
    assert stack.size() == 1
    assert stack.peek() == 13
    assert stack.size() == 1
    assert stack.pop() == 13
    assert stack.size() == 0
    assert stack.peek() is None
    assert stack.pop() is None

    stack.push(11)
    stack.push(12)
    assert stack.size() == 2
    assert stack.peek() == 12
    assert stack.pop() == 12
    assert stack.size() == 1
    assert stack.peek() == 11
