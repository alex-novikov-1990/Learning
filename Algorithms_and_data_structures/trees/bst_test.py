"""Tests for BST."""

from bst import BST


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


    assert bst.Count() == 14
    for i in range(0, 14):
        key = bst.Root.NodeKey
        bst.DeleteNodeByKey(key)
        assert not bst.FindNodeByKey(key).NodeHasKey
        assert bst.Count() == 13-i
        assert (bst.Root is None) == (i == 13)

def test_bst_walk():
    # prepare tree
    bst = BST(None)
    for i in range(1,5):
        step = int(32 / 2**i)
        for j in range(step, 32, step):
            result = int(j / step) % 2 == 1
            assert bst.AddKeyValue(j, j) == result
        assert bst.Count() == 2**i - 1
    bst.DeleteNodeByKey(20)

    # breadth-first
    assert list(map(lambda n: n.NodeValue, bst.WideAllNodes())) == \
        [16, 8, 24, 4, 12, 22, 28, 2, 6, 10, 14, 18, 26, 30]

    # depth-first in-order
    assert list(map(lambda n: n.NodeValue, bst.DeepAllNodes(0))) == \
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30]

    # depth-first post-order
    assert list(map(lambda n: n.NodeValue, bst.DeepAllNodes(1))) == \
        [2, 6, 4, 10, 14, 12, 8, 18, 22, 26, 30, 28, 24, 16]

    # depth-first pre-order
    assert list(map(lambda n: n.NodeValue, bst.DeepAllNodes(2))) == \
        [16, 8, 4, 2, 6, 12, 10, 14, 24, 22, 18, 28, 26, 30]

    # empty tree
    bst = BST(None)
    assert bst.WideAllNodes() == ()
    assert bst.DeepAllNodes(0) == ()
    assert bst.DeepAllNodes(1) == ()
    assert bst.DeepAllNodes(2) == ()

    # root-only tree
    bst.AddKeyValue(13, 13)
    assert len(bst.WideAllNodes()) == 1
    assert bst.WideAllNodes()[0].NodeValue == 13
    assert len(bst.DeepAllNodes(0)) == 1
    assert bst.DeepAllNodes(0)[0].NodeValue == 13
    assert len(bst.DeepAllNodes(1)) == 1
    assert bst.DeepAllNodes(1)[0].NodeValue == 13
    assert len(bst.DeepAllNodes(2)) == 1
    assert bst.DeepAllNodes(2)[0].NodeValue == 13
