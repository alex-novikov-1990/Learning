"""A module with a bracket sequence checker"""

from stack import Stack


def check_bracket_sequence(input_string: str):
    stack = Stack()
    for char in input_string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() != '(':
                return False

    return stack.size() == 0
