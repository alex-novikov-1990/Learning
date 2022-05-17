"""Tests for OrderedList and OrderedStringList."""

from ordered_list import OrderedList, OrderedStringList

def test_ordered_list_compare():
    ordered_list = OrderedList(asc=True)

    assert ordered_list.compare(1, 2) == -1
    assert ordered_list.compare(1, 100) == -1
    assert ordered_list.compare(2, 1) == 1
    assert ordered_list.compare(100, 1) == 1
    assert ordered_list.compare(1, 1) == 0
    assert ordered_list.compare(100, 100) == 0
    assert ordered_list.compare(-1, 2) == -1

def test_ordered_list_add_asc():
    ordered_list = OrderedList(asc=True)

    assert ordered_list.head is None
    assert ordered_list.tail is None

    ordered_list.add(1)

    assert ordered_list.head == ordered_list.tail
    assert ordered_list.head.value == 1
    node1 = ordered_list.head

    ordered_list.add(1)
    assert ordered_list.head == node1
    assert ordered_list.head.next == ordered_list.tail
    assert ordered_list.tail.value == 1
    node2 = ordered_list.tail

    ordered_list.add(1)
    assert node2.next == ordered_list.tail
    assert ordered_list.tail.value == 1
    node3 = ordered_list.tail

    ordered_list.add(0)
    assert ordered_list.head.value == 0
    assert ordered_list.head == node1.prev

    ordered_list.add(3)
    assert ordered_list.tail == node3.next
    assert ordered_list.tail.value == 3

def test_ordered_list_add_desc():
    ordered_list = OrderedList(asc=False)

    assert ordered_list.head is None
    assert ordered_list.tail is None
    assert ordered_list.len() == 0

    ordered_list.add(1)

    assert ordered_list.head == ordered_list.tail
    assert ordered_list.head.value == 1
    assert ordered_list.len() == 1
    node1 = ordered_list.head

    ordered_list.add(1)
    assert ordered_list.head == node1
    assert ordered_list.head.next == ordered_list.tail
    assert ordered_list.tail.value == 1
    assert ordered_list.len() == 2
    node2 = ordered_list.tail

    ordered_list.add(1)
    assert node2.next == ordered_list.tail
    assert ordered_list.tail.value == 1
    assert ordered_list.len() == 3
    node3 = ordered_list.tail

    ordered_list.add(3)
    assert ordered_list.head.value == 3
    assert ordered_list.head == node1.prev
    assert ordered_list.len() == 4

    ordered_list.add(-1)
    assert ordered_list.tail == node3.next
    assert ordered_list.tail.value == -1
    assert ordered_list.len() == 5

def test_ordered_list_find_asc():
    ordered_list = OrderedList(asc=True)

    assert ordered_list.find(0) is None

    ordered_list.add(0)
    node0 = ordered_list.find(0)
    assert node0 is not None

    ordered_list.add(0)
    ordered_list.add(-1)
    ordered_list.add(0)
    ordered_list.add(2)
    ordered_list.add(2)
    ordered_list.add(3)

    assert ordered_list.find(-2) is None
    assert ordered_list.find(10) is None
    assert ordered_list.find(0) == node0
    assert ordered_list.find(3) == ordered_list.tail
    assert ordered_list.find(2) == ordered_list.tail.prev.prev

def test_ordered_list_find_desc():
    ordered_list = OrderedList(asc=False)

    assert ordered_list.find(0) is None

    ordered_list.add(0)
    node0 = ordered_list.find(0)
    assert node0 is not None

    ordered_list.add(0)
    ordered_list.add(-1)
    ordered_list.add(0)
    ordered_list.add(2)
    ordered_list.add(2)
    ordered_list.add(3)

    assert ordered_list.find(-2) is None
    assert ordered_list.find(10) is None
    assert ordered_list.find(0) == node0
    assert ordered_list.find(3) == ordered_list.head
    assert ordered_list.find(2) == ordered_list.head.next
    assert ordered_list.find(0) == ordered_list.head.next.next.next

def test_ordered_list_delete_asc():
    ordered_list = OrderedList(asc=True)

    assert ordered_list.find(0) is None

    ordered_list.add(0)
    node0 = ordered_list.find(0)
    assert node0 is not None

    ordered_list.add(0)
    ordered_list.add(-1)
    ordered_list.add(0)
    ordered_list.add(2)
    ordered_list.add(2)
    ordered_list.add(3)

    assert ordered_list.find(0) == node0 # assume
    assert ordered_list.len() == 7
    ordered_list.delete(0)
    assert ordered_list.find(0) != node0
    assert ordered_list.len() == 6

    ordered_list.delete(-1)
    assert ordered_list.head.value == 0
    assert ordered_list.len() == 5

    ordered_list.delete(3)
    assert ordered_list.tail.value == 2
    assert ordered_list.len() == 4

def test_ordered_list_delete_desc():
    ordered_list = OrderedList(asc=False)

    assert ordered_list.find(0) is None

    ordered_list.add(0)
    node0 = ordered_list.find(0)
    assert node0 is not None

    ordered_list.add(0)
    ordered_list.add(-1)
    ordered_list.add(0)
    ordered_list.add(2)
    ordered_list.add(2)
    ordered_list.add(3)

    assert ordered_list.find(0) == node0 # assume
    assert ordered_list.len() == 7
    ordered_list.delete(0)
    assert ordered_list.find(0) != node0
    assert ordered_list.len() == 6

    ordered_list.delete(-1)
    assert ordered_list.tail.value == 0
    assert ordered_list.len() == 5

    ordered_list.delete(3)
    assert ordered_list.head.value == 2
    assert ordered_list.len() == 4

def test_ordered_string_list_asc():
    ordered_list = OrderedStringList(asc=True)
    ordered_list.add(" 123 ")
    ordered_list.add("  423  ")
    ordered_list.add("523")
    ordered_list.add("623")
    ordered_list.add("000")

    result = list(map(lambda n: n.value, ordered_list.get_all()))
    assert result[0] == "000"
    assert result[1] == " 123 "
    assert result[2] == "  423  "
    assert result[3] == "523"
    assert result[4] == "623"

def test_ordered_string_list_desc():
    ordered_list = OrderedStringList(asc=False)
    ordered_list.add(" 123 ")
    ordered_list.add("  423  ")
    ordered_list.add("523")
    ordered_list.add("623")
    ordered_list.add("000")

    result = list(map(lambda n: n.value, ordered_list.get_all()))
    assert result[0] == "623"
    assert result[1] == "523"
    assert result[2] == "  423  "
    assert result[3] == " 123 "
    assert result[4] == "000"
