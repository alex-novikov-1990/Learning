"""Tests for SimpleTree."""

from simple_tree import SimpleTree, SimpleTreeNode


def test_tree_building_and_counts():
    node1 = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, None)
    node3 = SimpleTreeNode(3, None)
    node4 = SimpleTreeNode(4, None)

    tree = SimpleTree(None)
    assert tree.Root is None
    assert tree.Count() == 0
    assert tree.LeafCount() == 0

    tree.AddChild(None, node1)
    assert tree.Root == node1
    assert not node1.Children
    assert node1.Parent is None
    assert tree.Count() == 1
    assert tree.LeafCount() == 1

    tree.AddChild(tree.Root, node2)
    assert tree.Root == node1
    assert node1.Children == [node2]
    assert node1.Parent is None
    assert node2.Parent == node1
    assert not node2.Children
    assert tree.Count() == 2
    assert tree.LeafCount() == 1

    tree.AddChild(tree.Root, node3)
    assert node1.Children == [node2, node3]
    assert node3.Parent == node1
    assert tree.Count() == 3
    assert tree.LeafCount() == 2

    tree.AddChild(node2, node4)
    assert len(node2.Children) == 1
    assert node4 in node2.Children
    assert node4.Parent == node2
    assert tree.Count() == 4
    assert tree.LeafCount() == 2

def test_tree_node_removal():
    tree = SimpleTree(None)
    node1 = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, None)
    node3 = SimpleTreeNode(3, None)
    node4 = SimpleTreeNode(4, None)
    tree.AddChild(None, node1)
    tree.AddChild(tree.Root, node2)
    tree.AddChild(tree.Root, node3)
    tree.AddChild(node2, node4)
    assert tree.Count() == 4 # asume
    assert tree.LeafCount() == 2 # asume

    tree.DeleteNode(node2)
    assert tree.Count() == 2
    assert tree.LeafCount() == 1
    assert node2.Parent is None
    assert node1.Children == [node3]

def test_tree_node_collection():
    tree = SimpleTree(None)
    node1 = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, None)
    node3 = SimpleTreeNode(3, None)
    node4 = SimpleTreeNode(4, None)
    tree.AddChild(None, node1)
    tree.AddChild(tree.Root, node2)
    tree.AddChild(tree.Root, node3)
    tree.AddChild(node2, node4)

    assert set(tree.GetAllNodes()) == set([node1, node2, node3, node4])

def test_tree_node_move():
    tree = SimpleTree(None)
    node1 = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, None)
    node3 = SimpleTreeNode(3, None)
    node4 = SimpleTreeNode(4, None)
    tree.AddChild(None, node1)
    tree.AddChild(tree.Root, node2)
    tree.AddChild(tree.Root, node3)
    tree.AddChild(node2, node4)
    assert tree.Count() == 4 # asume
    assert tree.LeafCount() == 2 # asume

    tree.MoveNode(node2, node3)
    assert tree.Count() == 4
    assert tree.LeafCount() == 1
    assert node2.Parent == node3
    assert node3.Children == [node2]

def test_tree_node_find():
    tree = SimpleTree(None)
    node1 = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, None)
    node3 = SimpleTreeNode(1, None)
    node4 = SimpleTreeNode(2, None)
    node5 = SimpleTreeNode(1, None)
    tree.AddChild(None, node1)
    tree.AddChild(tree.Root, node2)
    tree.AddChild(tree.Root, node3)
    tree.AddChild(node2, node4)
    tree.AddChild(node2, node5)
    assert tree.Count() == 5 # asume
    assert tree.LeafCount() == 3 # asume

    assert set(tree.FindNodesByValue(1)) == set([node1, node3, node5])

def test_tree_node_levels():
    tree = SimpleTree(None)
    node1 = SimpleTreeNode(1, None)
    node2 = SimpleTreeNode(2, None)
    node3 = SimpleTreeNode(1, None)
    node4 = SimpleTreeNode(2, None)
    node5 = SimpleTreeNode(1, None)
    tree.AddChild(None, node1)
    tree.AddChild(tree.Root, node2)
    tree.AddChild(tree.Root, node3)
    tree.AddChild(node2, node4)
    tree.AddChild(node4, node5)
    assert tree.Count() == 5 # asume
    assert tree.LeafCount() == 2 # asume

    tree.fill_node_levels()
    assert node1.level == 0
    assert node2.level == 1
    assert node3.level == 1
    assert node4.level == 2
    assert node5.level == 3

def test_even_trees():
    tree = SimpleTree(None)
    assert tree.EvenTrees() == []

    tree = SimpleTree(None)
    tree.AddChild(None, SimpleTreeNode(0, None))
    tree.AddChild(tree.Root, SimpleTreeNode(1, None))
    assert tree.EvenTrees() == []

    tree = SimpleTree(None)
    nodes = [SimpleTreeNode(1, None) for _ in range(10)]
    tree.AddChild(None, nodes[0])
    tree.AddChild(nodes[0], nodes[1])
    tree.AddChild(nodes[1], nodes[4])
    tree.AddChild(nodes[1], nodes[6])
    tree.AddChild(nodes[0], nodes[2])
    tree.AddChild(nodes[2], nodes[3])
    tree.AddChild(nodes[0], nodes[5])
    tree.AddChild(nodes[5], nodes[7])
    tree.AddChild(nodes[7], nodes[8])
    tree.AddChild(nodes[7], nodes[9])

    assert tree.EvenTrees() == [nodes[0], nodes[2], nodes[0], nodes[5]]
