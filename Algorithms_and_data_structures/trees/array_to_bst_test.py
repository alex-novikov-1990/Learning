"""Tests for aBST."""

import pytest
from random import shuffle

from array_to_bst import GenerateBBSTArray


def test():
    assert GenerateBBSTArray([1]) == [1]
    assert GenerateBBSTArray([1,2,3]) == [2,1,3]

    with pytest.raises(ValueError):
        assert GenerateBBSTArray([1,2])

    with pytest.raises(ValueError):
        assert GenerateBBSTArray([1,2,3,4])

    bst2 = [16,8,24,4,12,20,28]
    for _ in range(10):
        bst2_test = bst2.copy()
        shuffle(bst2_test)
        assert GenerateBBSTArray(bst2_test) == bst2
