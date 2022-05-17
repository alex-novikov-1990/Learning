"""Tests for a postfix notation calculator"""

import pytest

from stack_calc import calculate


def test_calc():
    input_string = "1 2 + 3 * ="
    result = calculate(input_string)
    assert result == 9

    input_string = "8 2 + 5 * 9 + ="
    result = calculate(input_string)
    assert result == 59

    with pytest.raises(ValueError):
        calculate("2 + 5 * 9 + =")

    with pytest.raises(ValueError):
        calculate("8 2 + * 9 + =")

    with pytest.raises(ValueError):
        calculate("8 2 + 5 * 9 =")

    with pytest.raises(ValueError):
        calculate("=")

    with pytest.raises(ValueError):
        calculate("8 2 + 5 * 9")

    with pytest.raises(ValueError):
        calculate("8 2 5 * 9 + =")

    assert calculate("8 2 + 5 / =") == 2
    assert calculate("5 2 * 5 - =") == 5
    assert calculate("1 2 + 3 4 + * =") == 21 # (1+2) * (3+4)
