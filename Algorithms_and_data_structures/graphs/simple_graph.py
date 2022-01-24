"""A simple example of graph."""


class Vertex:
    """A vertex of a simple graph."""

    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:
    """Graph with edges defined as an adjacency matrix"""

    def __init__(self, size):
        # TODO: rename "max_vertex" -> "capacity", "vertex" -> "vertices"
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        """v is value"""
        index = 0
        while self.vertex[index] is not None:
            index += 1
            if index >= self.max_vertex:
                raise ValueError("Capacity is exceeded")

        self.vertex[index] = Vertex(v)

    def RemoveVertex(self, v):
        """v is index"""
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        """v1, v2 is indices"""
        return self.m_adjacency[v1][v2] > 0

    def AddEdge(self, v1, v2):
        """v1, v2 is indices"""

        if self.vertex[v1] is None or self.vertex[v2] is None:
            return

        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        """v1, v2 is indices"""
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        """VFrom and VTo are indices. Searches a path between vertices and
        returns [VFrom, ..., Vto] array of indices if the path exists
        or [] if it doesn't."""

        if self.vertex[VFrom] is None:
            return []

        if VFrom == VTo:
            return [self.vertex[VFrom]]

        path = []
        for v in self.vertex:
            v.Hit = False

        def search(v_id):
            path.append(self.vertex[v_id])
            self.vertex[v_id].Hit = True
            if self.m_adjacency[v_id][VTo] == 1:
                path.append(self.vertex[VTo])
                return True

            for i in range(self.max_vertex):
                if self.m_adjacency[v_id][i] == 1 and \
                   not self.vertex[i].Hit and \
                   search(i):
                    return True

            path.pop()
            return False

        search(VFrom)
        return path

    def BreadthFirstSearch(self, VFrom, VTo):
        """VFrom and VTo are indices. Searches a path between vertices and
        returns [VFrom, ..., Vto] array of indices if the path exists
        or [] if it doesn't."""

        if self.vertex[VFrom] is None:
            return []

        if VFrom == VTo:
            return [self.vertex[VFrom]]

        for v in self.vertex:
            v.Hit = False
            v.Path = None

        queue = [] # deque
        queue.append(VFrom)
        self.vertex[VFrom].Hit = True
        self.vertex[VFrom].Path = [self.vertex[VFrom]]
        while True:
            current = queue.pop(0)
            if current == VTo:
                return self.vertex[current].Path

            for i in range(self.max_vertex):
                if self.m_adjacency[current][i] == 1 and \
                   not self.vertex[i].Hit:
                    self.vertex[i].Hit = True
                    self.vertex[i].Path = \
                        self.vertex[current].Path + \
                        [self.vertex[i]]
                    queue.append(i)

            if len(queue) == 0:
                return []
