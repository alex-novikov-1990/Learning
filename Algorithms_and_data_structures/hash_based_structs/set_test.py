"""Tests for PowerSet."""

import string
import random

from set import PowerSet


# 1e-20 probability to repeat the same string if random is really random
def get_random_string():
    return ''.join(
        random.choice(string.printable)
        for _ in range(10)
    )

def test_single_set_operations():
    """Test for put, get, remove and size"""

    the_set = PowerSet()

    # empty
    assert the_set.size() == 0
    assert not the_set.get("a")
    assert not the_set.remove("a")

    # put 50000 values
    expected = []
    for _ in range(50000):
        next_string = get_random_string()
        expected.append(next_string)
        the_set.put(next_string)
        assert the_set.get(next_string)
        assert the_set.size() == len(expected)

    # check 50000 values
    assert the_set.size() == 50000
    for value in expected:
        assert the_set.get(value)

    # check not-in-the-set string
    not_in_set = get_random_string()
    assert not the_set.get(not_in_set)
    assert not the_set.remove(not_in_set)
    assert the_set.size() == 50000

    # put the same 50000 values again
    for value in expected:
        the_set.put(value)

    # check 50000 values
    assert the_set.size() == 50000
    for value in expected:
        assert the_set.get(value)

    # remove last 40000 values
    for i in range(10000, 50000):
        assert the_set.remove(expected[i])

    # check
    assert the_set.size() == 10000
    for i, value in enumerate(expected):
        assert the_set.get(value) == (i < 10000)

    # put last 40000 back
    for i in range(10000, 50000):
        the_set.put(expected[i])

    # check
    assert the_set.size() == 50000
    for value in expected:
        assert the_set.get(value)

def test_two_sets_operations():
    empty_set = PowerSet()
    set_1 = PowerSet()
    set_1.put('1')
    set_1.put('2')
    set_2 = PowerSet()
    set_2.put('2')
    set_2.put('3')
    set_3 = PowerSet()
    set_3.put('4')

    # intersection
    assert empty_set.intersection(set_1).size() == 0
    assert set_1.intersection(empty_set).size() == 0
    assert set_1.intersection(set_3).size() == 0
    intersection_1 = set_1.intersection(set_2)
    assert intersection_1.size() == 1
    assert intersection_1.get('2')
    intersection_2 = set_1.intersection(set_1)
    assert intersection_2.size() == 2
    assert intersection_2.get('1')
    assert intersection_2.get('2')

    # union
    union_1 = empty_set.union(set_1)
    union_2 = set_1.union(empty_set)
    assert union_1.size() == 2
    assert union_2.size() == 2
    for value in ['1', '2']:
        assert union_1.get(value)
        assert union_2.get(value)

    union_3 = set_3.union(set_1)
    union_4 = set_1.union(set_3)
    assert union_3.size() == 3
    assert union_4.size() == 3
    for value in ['1', '2', '4']:
        assert union_3.get(value)
        assert union_4.get(value)

    union_5 = set_2.union(set_1)
    union_6 = set_1.union(set_2)
    assert union_5.size() == 3
    assert union_6.size() == 3
    for value in ['1', '2', '3']:
        assert union_5.get(value)
        assert union_6.get(value)

    # difference
    difference_1 = empty_set.difference(set_1)
    difference_2 = set_1.difference(set_1)
    assert difference_1.size() == 0
    assert difference_2.size() == 0

    difference_3 = set_2.difference(set_1)
    difference_4 = set_1.difference(set_2)
    assert difference_3.size() == 1
    assert difference_4.size() == 1
    assert difference_3.get('3')
    assert difference_4.get('1')

    difference_5 = set_1.difference(set_3)
    assert difference_5.size() == 2
    assert difference_5.get('1')
    assert difference_5.get('2')

    # issubset
    set_4 = PowerSet()
    set_4.put('1')

    assert set_1.issubset(set_1)
    assert set_1.issubset(empty_set)
    assert not empty_set.issubset(set_1)
    assert not set_3.issubset(set_1)
    assert set_1.issubset(set_4)
    assert not set_4.issubset(set_1)
    assert empty_set.issubset(empty_set)
