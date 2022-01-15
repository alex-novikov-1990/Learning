class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0

class BalancedBST:

    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        if a == []:
            return
        sorted_a = sorted(a)

        def subtree(arr, parent):
            if len(arr) == 0:
                return None

            center = int(len(arr) / 2)
            node = BSTNode(arr[center], parent)
            node.Level = 0 if parent is None else parent.Level + 1
            node.LeftChild = subtree(arr[:center], node)
            node.RightChild = subtree(arr[center+1:], node)
            return node

        self.Root = subtree(sorted_a, None)

    def IsBalanced(self, root_node):
        def check_node(node):
            if node is None:
                return (True, 0)
            (l_ok, l_depth) = check_node(node.LeftChild)
            (r_ok, r_depth) = check_node(node.RightChild)
            if r_depth > l_depth:
                ok = l_ok and r_ok and (r_depth - l_depth <= 1)
                depth = r_depth + 1
            else:
                ok = l_ok and r_ok and (l_depth - r_depth <= 1)
                depth = l_depth + 1
            return (ok, depth)

        return check_node(root_node)[0]
