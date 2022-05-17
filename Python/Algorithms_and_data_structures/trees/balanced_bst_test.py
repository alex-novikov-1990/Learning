"""Tests for BalancedBST."""

from balanced_bst import BSTNode, BalancedBST


def test_IsBalanced():
    bst = BalancedBST()

    root = BSTNode(16, None)
    assert bst.IsBalanced(root)

    l = BSTNode(8, root)
    root.LeftChild = l
    assert bst.IsBalanced(root)

    ll = BSTNode(4, l)
    l.LeftChild = ll
    assert not bst.IsBalanced(root)

    r = BSTNode(24, root)
    root.RightChild = r
    assert bst.IsBalanced(root)

    rr = BSTNode(28, r)
    r.RightChild = rr
    assert bst.IsBalanced(root)

    lll = BSTNode(2, ll)
    ll.LeftChild = lll
    assert not bst.IsBalanced(root)

    lr = BSTNode(12, l)
    l.RightChild = lr
    assert bst.IsBalanced(root)

def test_GenerateTree():
    bst = BalancedBST()

    bst.GenerateTree([])
    assert bst.Root is None

    bst.GenerateTree([16])
    check_tree_integrity(bst)
    assert bst.Root.NodeKey == 16
    assert bst.Root.LeftChild is None
    assert bst.Root.RightChild is None

    bst.GenerateTree([16, 8])
    check_tree_integrity(bst)
    assert bst.Root.NodeKey == 16
    assert bst.Root.LeftChild.NodeKey == 8
    assert bst.Root.LeftChild.LeftChild is None
    assert bst.Root.LeftChild.RightChild is None
    assert bst.Root.RightChild is None

    bst.GenerateTree([1, 2, 3, 4, 5])
    check_tree_integrity(bst)
    assert bst.IsBalanced(bst.Root)
    assert bst.Root.NodeKey == 3
    assert bst.Root.LeftChild.NodeKey == 2
    assert bst.Root.LeftChild.LeftChild.NodeKey == 1
    assert bst.Root.LeftChild.LeftChild.LeftChild is None
    assert bst.Root.LeftChild.LeftChild.RightChild is None
    assert bst.Root.LeftChild.RightChild is None
    assert bst.Root.RightChild.NodeKey == 5
    assert bst.Root.RightChild.LeftChild.NodeKey == 4
    assert bst.Root.RightChild.LeftChild.LeftChild is None
    assert bst.Root.RightChild.LeftChild.RightChild is None
    assert bst.Root.RightChild.RightChild is None

def check_tree_integrity(bst):
    if bst.Root is None:
        return

    def check_node(node):
        if node.LeftChild is not None:
            assert node.LeftChild.Parent is node
            assert node.LeftChild.Level == node.Level + 1
            assert node.LeftChild.NodeKey <= node.NodeKey
            check_node(node.LeftChild)
        if node.RightChild is not None:
            assert node.RightChild.Parent is node
            assert node.RightChild.Level == node.Level + 1
            assert node.RightChild.NodeKey >= node.NodeKey
            check_node(node.RightChild)

    assert bst.Root.Level == 0
    assert bst.Root.Parent is None
    check_node(bst.Root)
