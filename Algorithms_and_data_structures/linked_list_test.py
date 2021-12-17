"""Tests for LinkedList and its Node."""

from linked_list import LinkedList, Node
from linked_list_adder import add_linked_lists


def test_node():

    node0 = Node(0)
    node1 = Node(1)
    node0.next = node1

    assert node0.value == 0
    assert node0.next == node1
    assert node1.value == 1
    assert node1.next is None

def test_linked_list_appending():
    node1 = Node(11)
    node2 = Node(12)
    node3 = Node(13)

    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None

    linked_list.add_in_tail(node1)
    assert linked_list.head == node1
    assert linked_list.tail == linked_list.head
    assert linked_list.tail.next is None

    linked_list.add_in_tail(node2)
    assert linked_list.head == node1
    assert linked_list.head.next == node2
    assert linked_list.tail == node2
    assert linked_list.tail.next is None

    linked_list.add_in_tail(node3)
    assert linked_list.head == node1
    assert linked_list.head.next == node2
    assert node2.next == node3
    assert linked_list.tail == node3
    assert linked_list.tail.next is None

def test_linked_list_heterogeneity():
    node1 = Node(None)
    node2 = Node(1)
    node3 = Node("1")

    linked_list = LinkedList()
    linked_list.add_in_tail(node1)
    linked_list.add_in_tail(node2)
    linked_list.add_in_tail(node3)

    assert linked_list.head == node1
    assert linked_list.head.next == node2
    assert linked_list.tail == node3

def test_linked_list_print(capsys):
    linked_list = LinkedList()
    linked_list.print_all_nodes()
    linked_list.add_in_tail(Node(11))
    linked_list.print_all_nodes()
    linked_list.add_in_tail(Node(12))
    linked_list.print_all_nodes()
    linked_list.add_in_tail(Node(13))
    linked_list.print_all_nodes()

    captured = capsys.readouterr()
    expected = '\n'.join(['11', '11', '12', '11', '12', '13']) + '\n'
    assert captured.out == expected

def test_linked_list_find():
    node1 = Node(11)
    node2 = Node(13)
    node3 = Node(13)
    node4 = Node(13)

    linked_list = LinkedList()

    found = linked_list.find(0)
    assert found is None

    linked_list.add_in_tail(node1)

    found = linked_list.find(11)
    assert found == node1

    linked_list.add_in_tail(node2)
    linked_list.add_in_tail(node3)
    linked_list.add_in_tail(node4)

    found = linked_list.find(0)
    assert found is None

    found = linked_list.find(13)
    assert found == node2

def test_linked_list_delete():
    linked_list = LinkedList()
    linked_list.delete(1)
    assert linked_list.head is None
    assert linked_list.tail is None

    linked_list = LinkedList()
    linked_list.add_in_tail(Node(1))
    linked_list.delete(1)
    assert linked_list.head is None
    assert linked_list.tail is None

    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(3)
    node4 = Node(3)
    node5 = Node(4)
    linked_list = LinkedList()
    linked_list.add_in_tail(node1)
    linked_list.add_in_tail(node2)
    linked_list.add_in_tail(node3)
    linked_list.add_in_tail(node4)
    linked_list.add_in_tail(node5)

    linked_list.delete(1)
    assert linked_list.head == node2

    linked_list.delete(3)
    assert node2.next == node4

    linked_list.delete(4)
    assert linked_list.tail == node4
    assert node4.next is None

def test_linked_list_delete_with_all():
    linked_list = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(node1)
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(node2)
    linked_list.add_in_tail(node3)
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(node4)
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(Node(0))

    linked_list.delete(0, all=True)
    assert linked_list.head == node1
    assert node1.next == node2
    assert node2.next == node3
    assert node3.next == node4
    assert linked_list.tail == node4

def test_linked_list_clean():
    linked_list = LinkedList()
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(Node(0))

    linked_list.clean()
    assert linked_list.head is None
    assert linked_list.tail is None

def test_linked_list_len():
    linked_list = LinkedList()
    assert linked_list.len() == 0

    linked_list.add_in_tail(Node(0))
    assert linked_list.len() == 1

    linked_list.add_in_tail(Node(0))
    assert linked_list.len() == 2

    linked_list.add_in_tail(Node(0))
    assert linked_list.len() == 3

def test_linked_list_find_all():
    linked_list = LinkedList()
    assert len(linked_list.find_all(0)) == 0

    linked_list = LinkedList()
    linked_list.add_in_tail(Node(1))
    assert len(linked_list.find_all(0)) == 0

    linked_list = LinkedList()
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(Node(1))
    linked_list.add_in_tail(Node(0))
    linked_list.add_in_tail(Node(3))
    linked_list.add_in_tail(Node(0))

    result = linked_list.find_all(0)
    assert len(result) == 3
    assert all(map(lambda n: n.value == 0, result))

def test_linked_list_insert():
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    linked_list = LinkedList()
    linked_list.add_in_tail(node2)
    linked_list.add_in_tail(node4)

    linked_list.insert(afterNode=None,newNode=node1)
    assert linked_list.head == node1
    assert node1.next == node2

    linked_list.insert(afterNode=node2,newNode=node3)
    assert node2.next == node3
    assert node3.next == node4

    linked_list.insert(afterNode=node4,newNode=node5)
    assert node4.next == node5
    assert linked_list.tail == node5

    node1 = Node(1)
    node2 = Node(1)
    linked_list = LinkedList()
    linked_list.insert(afterNode=None,newNode=node1)
    assert linked_list.head == node1
    assert linked_list.tail == node1

    linked_list.insert(afterNode=node1,newNode=node2)
    assert linked_list.head == node1
    assert node1.next == node2
    assert linked_list.tail == node2

def test_linked_list_adder():
    linked_list1 = LinkedList()
    linked_list1.add_in_tail(Node(1))
    linked_list1.add_in_tail(Node(1))
    linked_list1.add_in_tail(Node(1))

    linked_list2 = LinkedList()
    linked_list2.add_in_tail(Node(3))
    linked_list2.add_in_tail(Node(4))
    assert add_linked_lists(linked_list1, linked_list2) is None

    linked_list2.add_in_tail(Node(5))
    result = add_linked_lists(linked_list1, linked_list2)
    assert result is not None
    assert result.head.value == 4
    assert result.head.next.value == 5
    assert result.head.next.next.value == 6
    assert result.tail.value == 6
