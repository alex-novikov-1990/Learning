"""An example of binary search tree"""


class BSTNode:
    """The node of binary search tree"""

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    """The search result for binary search tree"""

    def __init__(self):
        self.Node = None # None if there is no nodes in the tree

        self.NodeHasKey = False # if found
        self.ToLeft = False # if not found,
        # but expected to the left of the current

class BST:
    """The binary search tree"""

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        bst_find = BSTFind()
        if self.Root is None:
            return bst_find

        bst_find.Node = self.Root
        while True:
            if bst_find.Node.NodeKey == key:
                bst_find.NodeHasKey = True
                return bst_find
            if key > bst_find.Node.NodeKey:
                if bst_find.Node.RightChild is None:
                    return bst_find

                bst_find.Node = bst_find.Node.RightChild
            else:
                if bst_find.Node.LeftChild is None:
                    bst_find.ToLeft = True
                    return bst_find

                bst_find.Node = bst_find.Node.LeftChild

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        found = self.FindNodeByKey(key)
        if found.NodeHasKey:
            return False

        if found.ToLeft:
            found.Node.LeftChild = BSTNode(key, val, found.Node)
        else:
            found.Node.RightChild = BSTNode(key, val, found.Node)

        return True

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return None

        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
        else:
            while node.LeftChild is not None:
                node = node.LeftChild

        return node

    def DeleteNodeByKey(self, key):
        if self.Root is None:
            return False

        found = self.FindNodeByKey(key)
        if not found.NodeHasKey:
            return False

        to_delete = found.Node

        # find and extract a replacement node
        replacement = None

        if to_delete.RightChild is not None:
            # find in right subtree
            replacement = to_delete.RightChild
            while replacement.LeftChild is not None:
                replacement = replacement.LeftChild

            # extract
            if replacement.RightChild is not None:
                if replacement.Parent != to_delete:
                    replacement.Parent.LeftChild = replacement.RightChild
                else:
                    replacement.Parent.RightChild = replacement.RightChild
                replacement.RightChild.Parent = replacement.Parent
                replacement.Parent = None
                replacement.RightChild = None
            else:
                if replacement.Parent != to_delete:
                    replacement.Parent.LeftChild = None
                else:
                    replacement.Parent.RightChild = None
                replacement.Parent = None
            
        elif to_delete.LeftChild is not None:
            # find in left subtree
            replacement = to_delete.LeftChild
            while replacement.RightChild is not None:
                replacement = replacement.RightChild

            # extract
            if replacement.LeftChild is not None:
                if replacement.Parent != to_delete:
                    replacement.Parent.RightChild = replacement.LeftChild
                else:
                    replacement.Parent.LeftChild = replacement.LeftChild

                replacement.LeftChild.Parent = replacement.Parent
                replacement.Parent = None
                replacement.RightChild = None
            else:
                if replacement.Parent != to_delete:
                    replacement.Parent.RightChild = None
                else:
                    replacement.Parent.LeftChild = None
                replacement.Parent = None

        # delete
        if to_delete.Parent is None:
            pass
        elif to_delete.Parent.RightChild == to_delete:
            to_delete.Parent.RightChild = replacement
        elif to_delete.Parent.LeftChild == to_delete:
            to_delete.Parent.LeftChild = replacement
        else:
            raise RuntimeError()
        
        if to_delete.LeftChild is not None:
            to_delete.LeftChild.Parent = replacement

        if to_delete.RightChild is not None:
            to_delete.RightChild.Parent = replacement

        if replacement is not None:
            replacement.Parent = to_delete.Parent
            replacement.LeftChild = to_delete.LeftChild
            replacement.RightChild = to_delete.RightChild

        to_delete.Parent = None
        to_delete.LeftChild = None
        to_delete.RightChild = None

        if self.Root == to_delete:
            self.Root = replacement

        return True

    def Count(self):
        if self.Root is None:
            return 0

        def count(node):
            result = 1
            if node.LeftChild is not None:
                result += count(node.LeftChild)
            if node.RightChild is not None:
                result += count(node.RightChild)
            return result

        return count(self.Root)
