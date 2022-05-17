"""Tests for aBST."""

from array_bst import aBST


def test_abst():
    abst = aBST(2) # 1+2+4=7
    assert abst.Tree == [None] * 7

    assert abst.FindKeyIndex(16) == 0 # by task design
    assert abst.AddKey(16) == 0
    assert abst.Tree == [16, None,None, None,None,None,None]
    assert abst.FindKeyIndex(16) == 0

    assert abst.FindKeyIndex(15) == -1
    assert abst.FindKeyIndex(24) == -2
    assert abst.FindKeyIndex(28) == -2
    assert abst.AddKey(24) == 2
    assert abst.Tree == [16, None,24, None,None,None,None]
    assert abst.FindKeyIndex(24) == 2

    assert abst.FindKeyIndex(23) == -5
    assert abst.FindKeyIndex(25) == -6
    assert abst.FindKeyIndex(28) == -6
    assert abst.AddKey(28) == 6
    assert abst.Tree == [16, None,24, None,None,None,28]
    assert abst.FindKeyIndex(28) == 6

    assert abst.FindKeyIndex(20) == -5
    assert abst.AddKey(20) == 5
    assert abst.Tree == [16, None,24, None,None,20,28]
    assert abst.FindKeyIndex(20) == 5

    assert abst.AddKey(30) == -1
