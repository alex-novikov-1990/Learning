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