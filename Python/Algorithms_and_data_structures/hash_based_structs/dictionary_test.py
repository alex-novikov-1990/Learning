"""Tests for NativeDictionary."""

import string
import random

from dictionary import NativeDictionary


# 1e-20 probability to repeat the same string if random is really random
def get_random_string():
    return ''.join(
        random.choice(string.printable)
        for _ in range(10)
    )

def test_dictionary_hash_fun():
    dictionary = NativeDictionary(17)

    random_strings = [get_random_string() for _ in range(1000)]
    hashes = list(map(dictionary.hash_fun, random_strings))

    # next two lines have a compound ~1e-26 probability
    # to give false negative result
    assert hashes.index(0) >= 0
    assert hashes.index(16) >= 0
    for string_hash in hashes:
        assert string_hash >= 0
        assert string_hash < 17

def test_dictionary():
    dictionary = NativeDictionary(17)

    # we need to generate a list because hash function is not deterministic
    strings = [get_random_string() for _ in range(18)]

    for i in range(17):
        dictionary.put(strings[i], i)
        assert dictionary.is_key(strings[i])
        assert not dictionary.is_key(strings[i+1])
        assert dictionary.get(strings[i]) == i
        assert dictionary.get(strings[i+1]) is None

    for i in range(17):
        assert dictionary.get(strings[i]) == i

def test_dictionary_collisions():
    dictionary = NativeDictionary(17)

    # we need to generate a list because hash function is not deterministic
    hash0_strings = []
    while len(hash0_strings) < 18:
        next_string = get_random_string()
        if dictionary.hash_fun(next_string) == 0:
            hash0_strings.append(next_string)

    for i in range(17):
        dictionary.put(hash0_strings[i], i)
        assert dictionary.is_key(hash0_strings[i])
        assert not dictionary.is_key(hash0_strings[i+1])
        assert dictionary.get(hash0_strings[i]) == i
        assert dictionary.get(hash0_strings[i+1]) is None

    dictionary.put(hash0_strings[3], "abc")

    for i in range(17):
        assert dictionary.get(hash0_strings[i]) == (i if i != 3 else "abc")
