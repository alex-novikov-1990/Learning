"""Tests for NativeCache."""

import string
import random

from cache import NativeCache


# 1e-20 probability to repeat the same string if random is really random
def get_random_string():
    return ''.join(
        random.choice(string.printable)
        for _ in range(10)
    )

def test_cache_hash_fun():
    cache = NativeCache(17)

    random_strings = [get_random_string() for _ in range(1000)]
    hashes = list(map(cache.hash_fun, random_strings))

    # next two lines have a compound ~1e-26 probability
    # to give false negative result
    assert hashes.index(0) >= 0
    assert hashes.index(16) >= 0
    for string_hash in hashes:
        assert string_hash >= 0
        assert string_hash < 17

def test_cache():
    cache = NativeCache(23)

    strings = [get_random_string() for _ in range(1000)]

    hits = []
    in_cache = []
    values = []
    for i in range(1000):
        assert not cache.is_key(strings[i])
        assert cache.get(strings[i]) is None

        cache.put(strings[i], i)
        index = i
        if i < 23:
            hits.append(0)
            in_cache.append(strings[i])
            values.append(i)
        else:
            removed = [j for j in range(23) if not cache.is_key(in_cache[j])]
            assert len(removed) == 1
            index = removed[0]
            assert hits[index] == min(hits)
            hits[index] = 0
            in_cache[index] = strings[i]
            values[index] = i

        # hit random entries
        for _ in range(10):
            random_i = random.randint(0, min(i,22))
            assert cache.get(in_cache[random_i]) == values[random_i]
            hits[random_i] += 1

        assert cache.is_key(strings[i])
        assert cache.get(strings[i]) == i
        hits[index] += 1

    for i in range(23):
        assert cache.get(in_cache[i]) == values[i]
