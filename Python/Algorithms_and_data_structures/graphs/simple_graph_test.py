"""Tests for SimpleGraph."""

from simple_graph import SimpleGraph, Vertex


def test_graph_vertices():
    graph = SimpleGraph(4)
    assert graph.vertex == [None] * 4

    graph.AddVertex(None)
    assert_v_eq(graph.vertex, [Vertex(None), None, None, None])

    graph.AddVertex(0)
    assert_v_eq(graph.vertex, [Vertex(None), Vertex(0), None, None])

    graph.RemoveVertex(2)
    assert_v_eq(graph.vertex, [Vertex(None), Vertex(0), None, None])

    graph.RemoveVertex(0)
    assert_v_eq(graph.vertex, [None, Vertex(0), None, None])

    graph.AddVertex(2)
    assert_v_eq(graph.vertex, [Vertex(2), Vertex(0), None, None])

    graph.AddVertex(0)
    graph.AddVertex(3)
    assert_v_eq(graph.vertex, [Vertex(2), Vertex(0), Vertex(0), Vertex(3)])

def test_graph_edges():
    no_edges = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    one_edge = [
        [0,0,1,0],
        [0,0,0,0],
        [1,0,0,0],
        [0,0,0,0]
    ]
    two_edges = [
        [1,0,1,0],
        [0,0,0,0],
        [1,0,0,0],
        [0,0,0,0]
    ]
    one_self_loop_edge = [
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    # empty graph - no edges
    graph = SimpleGraph(4)
    assert graph.m_adjacency == no_edges

    # prepare graph - no edges yet
    graph.AddVertex(0)
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.RemoveVertex(1)
    assert_v_eq(graph.vertex, [Vertex(0), None, Vertex(2), None])
    assert not graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(0,2)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == no_edges

    # incorrect operations - no effect
    graph.RemoveEdge(0,2)
    assert graph.m_adjacency == no_edges
    graph.AddEdge(1,1)
    graph.AddEdge(0,1)
    graph.AddEdge(2,3)
    graph.AddEdge(1,3)
    assert graph.m_adjacency == no_edges

    # add edge
    graph.AddEdge(0,2)
    assert graph.IsEdge(0,2)
    assert graph.IsEdge(2,0)
    assert not graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == one_edge

    # add self-loop edge
    graph.AddEdge(0,0)
    assert graph.IsEdge(0,2)
    assert graph.IsEdge(2,0)
    assert graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == two_edges

    # remove one of edges
    graph.RemoveEdge(0,0)
    assert graph.IsEdge(0,2)
    assert graph.IsEdge(2,0)
    assert not graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == one_edge

    # restore removed edge
    graph.AddEdge(0,0)
    assert graph.IsEdge(0,2)
    assert graph.IsEdge(2,0)
    assert graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == two_edges

    # remove vertex with one edge - should remove edge
    graph.RemoveVertex(2)
    assert not graph.IsEdge(0,2)
    assert not graph.IsEdge(2,0)
    assert graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == one_self_loop_edge

    # return vertex back - should not return edge
    graph.AddVertex(1)
    graph.AddVertex(2)
    graph.RemoveVertex(1)
    assert_v_eq(graph.vertex, [Vertex(0), None, Vertex(2), None])
    assert not graph.IsEdge(0,2)
    assert not graph.IsEdge(2,0)
    assert graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == one_self_loop_edge

    # restore removed edge
    graph.AddEdge(0,2)
    assert graph.IsEdge(0,2)
    assert graph.IsEdge(2,0)
    assert graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == two_edges

    # remove vertex with multiple edges including self-loop - should remove all
    graph.RemoveVertex(0)
    assert not graph.IsEdge(0,2)
    assert not graph.IsEdge(2,0)
    assert not graph.IsEdge(0,0)
    assert not graph.IsEdge(0,1)
    assert not graph.IsEdge(1,1)
    assert not graph.IsEdge(1,3)
    assert graph.m_adjacency == no_edges


def assert_v_eq(left, right):
    assert len(left) == len(right)
    for i in range(len(left)):
        assert left[i] is None and right[i] is None or \
            left[i].Value == right[i].Value

def test_graph_search():
    graph = SimpleGraph(7)
    for i in range(5):
        graph.AddVertex(i)
    graph.AddEdge(0, 1)
    graph.AddEdge(0, 2)
    graph.AddEdge(1, 2)
    graph.AddEdge(2, 3)

    for _ in range(2): # repeatability
        assert_eq(graph.DepthFirstSearch(0, 0), [0])
        assert_eq(graph.DepthFirstSearch(0, 3), [0, 1, 2, 3])
        assert_eq(graph.DepthFirstSearch(0, 4), [])
        assert_eq(graph.BreadthFirstSearch(0, 0), [0])
        assert_eq(graph.BreadthFirstSearch(0, 3), [0, 2, 3])
        assert_eq(graph.BreadthFirstSearch(0, 4), [])

def test_graph_weak_search():
    graph = SimpleGraph(12)
    assert_eq(graph.WeakVertices(), [])

    for i in range(9):
        graph.AddVertex(i)
    assert_eq(graph.WeakVertices(), [i for i in range(9)])

    graph.AddEdge(0, 1)
    graph.AddEdge(0, 2)
    graph.AddEdge(1, 3)
    graph.AddEdge(2, 3)
    assert_eq(graph.WeakVertices(), [i for i in range(9)])

    graph.AddEdge(1, 2)
    assert_eq(graph.WeakVertices(), [i for i in range(4,9)])

    graph.AddEdge(2, 5)
    graph.AddEdge(3, 4)
    graph.AddEdge(4, 5)
    graph.AddEdge(5, 6)
    graph.AddEdge(5, 7)
    assert_eq(graph.WeakVertices(), [i for i in range(4,9)])

    graph.AddEdge(6, 7)
    graph.AddEdge(6, 8)
    assert_eq(graph.WeakVertices(), [4, 8])

    graph.AddEdge(4, 7)
    assert_eq(graph.WeakVertices(), [8])

    graph.AddEdge(7, 8)
    assert_eq(graph.WeakVertices(), [])

def assert_eq(vertices, values):
    assert list(map(lambda v: v.Value, vertices)) == values
