"""A module with a postfix notation stack calcularor"""

from stack import Stack


def calculate(input_string: str):
    # populate input_stack
    input_stack = Stack()
    for item in reversed(input_string.split(' ')):
        if item in ("+", "-", "*", "/", "="):
            input_stack.push(item)
        elif item.isdigit():
            input_stack.push(int(item))
        else:
            raise ValueError(
                "Only '+', '-', '*', '/', '=' and integers are supported, " +
                "and they should be delimited by exactly one space."
                )

    # calculate
    args_buffer = Stack()
    while input_stack.size() > 0:
        item = input_stack.pop()

        if item in ("+", "-", "*", "/"):
            if args_buffer.size() <= 1:
                raise ValueError(f"Not enough arguments before '{item}'")

            right = args_buffer.pop()
            left = args_buffer.pop()
            if item == "+":
                result = left + right
            elif item == "-":
                result = left - right
            elif item == "*":
                result = left * right
            elif item == "/":
                result = left / right

            args_buffer.push(result)

        elif item == "=":
            if input_stack.size() != 0:
                raise ValueError("'=' should be at the end of the input string")

            if args_buffer.size() != 1:
                raise ValueError(
                    "There should be exactly one calculated argument before '='"
                    )

            return args_buffer.pop()

        else:
            args_buffer.push(item)

    raise ValueError("'=' is missed")
