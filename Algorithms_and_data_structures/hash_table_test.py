"""Tests for HashTable."""

import string
import random

from hash_table import HashTable


# 1e-20 probability to repeat the same string if random is really random
def get_random_string():
    return ''.join(
        random.choice(string.printable)
        for _ in range(10)
    )

def test_hash_table_hash_fun():
    hash_table = HashTable(17, 3)

    random_strings = [get_random_string() for _ in range(1000)]
    hashes = list(map(hash_table.hash_fun, random_strings))

    # next two lines have a compound ~1e-26 probability
    # to give false negative result
    assert hashes.index(0) >= 0
    assert hashes.index(16) >= 0
    for string_hash in hashes:
        assert string_hash >= 0
        assert string_hash < 17

def test_hash_table_collisions():
    hash_table = HashTable(17, 3)

    # we need to generate a list because hash function is not deterministic
    hash0_strings = []
    while len(hash0_strings) < 18:
        next_string = get_random_string()
        if hash_table.hash_fun(next_string) == 0:
            hash0_strings.append(next_string)

    expected = [0, 3, 6, 9, 12, 15, 1, 4, 7, 10, 13, 16, 2, 5, 8, 11, 14, 17]
    for i in range(17):
        assert hash_table.seek_slot(hash0_strings[i]) == expected[i]
        assert hash_table.put(hash0_strings[i]) == expected[i]
        assert hash_table.find(hash0_strings[i]) == expected[i]

    assert hash_table.seek_slot(hash0_strings[17]) is None

    for i in range(17):
        assert hash_table.find(hash0_strings[i]) == expected[i]

def test_hash_table():
    hash_table = HashTable(17, 3)

    assert hash_table.find("a") is None

    strings = [get_random_string() for _ in range(18)]
    slots = []
    for i in range(17):
        slot = hash_table.seek_slot(strings[i])
        assert hash_table.put(strings[i]) == slot
        assert hash_table.find(strings[i]) == slot
        slots.append(slot)

    assert hash_table.seek_slot(strings[17]) is None

    for i in range(17):
        assert hash_table.find(strings[i]) == slots[i]
