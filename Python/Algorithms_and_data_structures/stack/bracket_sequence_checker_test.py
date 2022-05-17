"""Tests for a bracket sequence checker"""

from bracket_sequence_checker import check_bracket_sequence


def test_bracket_sequence_checker():
    assert check_bracket_sequence("")
    assert not check_bracket_sequence("(")
    assert not check_bracket_sequence(")")
    assert check_bracket_sequence("()")

    assert check_bracket_sequence("(()((())()))")
    assert not check_bracket_sequence("(()()(()")
    assert not check_bracket_sequence("())())")
    assert not check_bracket_sequence("))((")
    assert not check_bracket_sequence("((())")
