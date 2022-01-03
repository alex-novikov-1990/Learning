"""A simple example of tree"""

class SimpleTreeNode:
    """The node of SimpleTree"""

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []

class SimpleTree:
    """Simple tree"""

    def __init__(self, root):
        """The root could be None"""
        self.Root = root

    def __should_contain(self, node, arg_name):
        if self.Root is None:
            if node is None:
                return
            raise ValueError(f"{arg_name} doesn't belong to this tree")

        root = node
        while root.Parent is not None:
            root = root.Parent

        if self.Root != root:
            raise ValueError(f"{arg_name} doesn't belong to this tree")


    def AddChild(self, ParentNode, NewChild):
        if NewChild.Parent is not None:
            raise ValueError(
                "It is a tree, not a graph (new child has a parent already)"
            )

        if self.Root is None and ParentNode is None:
            self.Root = NewChild
            return

        self.__should_contain(ParentNode, "ParentNode")
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        self.__should_contain(NodeToDelete, "NodeToDelete")
        if self.Root == NodeToDelete:
            self.Root = None
            return

        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None:
            return []

        # depth first
        def collect(node):
            result = [node]
            result.extend([
                node
                for child in node.Children
                for node in collect(child)
            ])
            return result

        return collect(self.Root)

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []

        # depth first
        def find(node):
            result = [node] if node.NodeValue == val else []
            result.extend([
                node
                for child in node.Children
                for node in find(child)
                if node.NodeValue == val
            ])
            return result

        return find(self.Root)

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode == self.Root:
            raise ValueError("Can't move root node")

        # fail fast, save the tree
        self.__should_contain(NewParent, "NewParent")
        new_ancestor = NewParent
        while new_ancestor is not None:
            if new_ancestor == OriginalNode:
                raise ValueError("Can't move node to its own subtree")
            new_ancestor = new_ancestor.Parent

        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        if self.Root is None:
            return 0

        def count(node):
            return 1 + sum(map(count, node.Children))

        return count(self.Root)

    def LeafCount(self):
        if self.Root is None:
            return 0

        def count_leaves(node):
            return 1 if len(node.Children) == 0 \
                else sum(map(count_leaves, node.Children))

        return count_leaves(self.Root)

    def fill_node_levels(self):
        if self.Root is None:
            return

        def fill_levels(node, level=0):
            node.level = level
            for child in node.Children:
                fill_levels(child, level+1)

        fill_levels(self.Root)
