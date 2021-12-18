"""Tests for DynArray."""

import pytest

from dynamic_array import DynArray


def test_dynamic_array_creation():
    array = DynArray()

    assert len(array) == 0
    with pytest.raises(IndexError):
        assert array[0]

    array.append(123)
    assert len(array) == 1
    assert array[0] == 123
    with pytest.raises(IndexError):
        assert array[1]
    with pytest.raises(IndexError):
        assert array[-1]
    assert array.capacity == 16

    array = DynArray()
    for i in range(64):
        array.append(i)

    assert array[0] == 0
    assert array[63] == 63
    assert len(array) == 64
    assert array.capacity == 64


def test_dynamic_array_insert():
    array = DynArray()
    assert array.capacity == 16 # asume

    for i in range(16):
        array.append(i)
    assert array.capacity == 16

    with pytest.raises(IndexError):
        assert array.insert(i=-1, itm=0)

    with pytest.raises(IndexError):
        assert array.insert(i=17, itm=0)

    array.insert(i=16, itm=16)
    assert array.capacity == 32
    assert len(array) == 17
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for i in range(17):
        assert array[i] == expected[i]

    array.insert(i=16, itm=17)
    assert len(array) == 18
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16]
    for i in range(18):
        assert array[i] == expected[i]

    array.insert(i=0, itm=18)
    expected = [18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16]
    for i in range(19):
        assert array[i] == expected[i]

def test_dynamic_array_delete():
    array = DynArray()
    for i in range(17):
        array.append(i)

    with pytest.raises(IndexError):
        assert array.delete(-1)

    with pytest.raises(IndexError):
        assert array.delete(17)

    assert array.capacity == 32 # asume
    array.delete(0)
    assert array.capacity == 32
    assert len(array) == 16

    array.delete(15)
    assert len(array) == 15
    assert array.capacity == 21 # int(32/1.5)

    array.delete(5)
    array.delete(5)
    array.delete(5)
    array.delete(5)
    assert len(array) == 11
    assert array.capacity == 21
    array.delete(5)
    assert len(array) == 10
    assert array.capacity == 16 # > int(21/1.5)
    expected = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]
    for i in range(10):
        assert array[i] == expected[i]
