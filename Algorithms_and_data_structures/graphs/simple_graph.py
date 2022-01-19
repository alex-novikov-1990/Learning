"""A simple example of graph."""


class Vertex:
    """A vertex of a simple graph."""

    def __init__(self, val):
        self.Value = val

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
