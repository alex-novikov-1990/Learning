"""Tests for BST."""

from bst import BST, BSTFind


def test_bst():
    bst = BST(None)
    assert bst.Count() == 0

    for i in range(1,5):
        step = int(32 / 2**i)
        for j in range(step, 32, step):
            result = int(j / step) % 2 == 1
            assert bst.AddKeyValue(j, j) == result
        assert bst.Count() == 2**i - 1

    assert bst.Count() == 15 # 16, 8+24, 4+12+20+28, 2+6+10+14+18+22+26+30

    found = bst.FindNodeByKey(7)
    assert not found.NodeHasKey
    assert found.Node.NodeValue == 6
    assert not found.ToLeft

    found = bst.FindNodeByKey(5)
    assert not found.NodeHasKey
    assert found.Node.NodeValue == 6
    assert found.ToLeft

    found = bst.FindNodeByKey(4)
    assert found.NodeHasKey
    assert found.Node.NodeKey == 4
    assert found.Node.NodeValue == 4
    assert found.Node.Parent.NodeKey == 8
    assert found.Node.Parent.LeftChild == found.Node
    assert found.Node.LeftChild.NodeKey == 2
    assert found.Node.RightChild.NodeKey == 6

    min_node = bst.FinMinMax(bst.Root, False)
    assert min_node.NodeKey == 2
    max_node = bst.FinMinMax(bst.Root, True)
    assert max_node.NodeKey == 30

    min_node = bst.FinMinMax(bst.Root.RightChild, False)
    assert min_node.NodeKey == 18
    max_node = bst.FinMinMax(bst.Root.LeftChild, True)
    assert max_node.NodeKey == 14

    node_20 = bst.FindNodeByKey(20).Node
    assert node_20.NodeKey == 20
    bst.DeleteNodeByKey(20)
    assert not bst.FindNodeByKey(20).NodeHasKey
    assert bst.FindNodeByKey(24).Node.LeftChild.NodeKey == 22
    assert bst.FindNodeByKey(22).Node.Parent.NodeKey == 24
