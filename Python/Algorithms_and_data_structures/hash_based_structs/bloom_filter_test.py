"""Tests for BloomFilter."""

from bloom_filter import BloomFilter


def test_bloom_filter_with_many_false_positives():
    bloom_filter = BloomFilter(32)

    strings = [
        "0123456789",
        "1234567890",
        "2345678901",
        "3456789012",
        "4567890123",
        "5678901234",
        "6789012345",
        "7890123456",
        "8901234567",
        "9012345678",
    ]
    false_positives_1 = [0, 2, 4, 6, 8]
    false_positives_2 = [1, 3, 5, 7, 9]

    # assume
    def hashes_are_equal(str1, str2):
        return (bloom_filter.hash1(str1) == bloom_filter.hash1(str2)) and \
               (bloom_filter.hash2(str1) == bloom_filter.hash2(str2))

    for i in range(10):
        for j in range(10):
            assert hashes_are_equal(strings[i], strings[j]) == ((i == j) or \
                # false positives
                ((i in false_positives_1) and (j in false_positives_1)) or \
                ((i in false_positives_2) and (j in false_positives_2))
            )

    # test
    for i in range(10):
        assert not bloom_filter.is_value(strings[i])

    for i in range(10):
        bloom_filter.add(strings[i])
        for j in range(10):
            is_value = bloom_filter.is_value(strings[j])
            if i == 0:
                assert is_value == (j in [0, 2, 4, 6, 8])
            else:
                assert is_value

def test_bloom_filter_with_one_false_positive():
    bloom_filter = BloomFilter(31)

    strings = [
        "0123456789",
        "1234567890",
        "2345678901",
        "3456789012",
        "4567890123",
        "5678901234",
        "6789012345",
        "7890123456",
        "8901234567",
        "9012345678",
    ]

    # assume
    def hashes_are_equal(str1, str2):
        return (bloom_filter.hash1(str1) == bloom_filter.hash1(str2)) and \
               (bloom_filter.hash2(str1) == bloom_filter.hash2(str2))

    for i in range(10):
        for j in range(10):
            assert hashes_are_equal(strings[i], strings[j]) == ((i == j))

    # test
    for i in range(10):
        assert not bloom_filter.is_value(strings[i])

    for i in range(10):
        bloom_filter.add(strings[i])
        for j in range(10):
            assert bloom_filter.is_value(strings[j]) == ((i >= j) or \
                ((i >= 3) and (j == 5))) # false positive

def test_bloom_filter_without_false_positives():
    bloom_filter = BloomFilter(30)

    strings = [
        "0123456789",
        "1234567890",
        "2345678901",
        "3456789012",
        "4567890123",
        "5678901234",
        "6789012345",
        "7890123456",
        "8901234567",
        "9012345678",
    ]

    # assume
    def hashes_are_equal(str1, str2):
        return (bloom_filter.hash1(str1) == bloom_filter.hash1(str2)) and \
               (bloom_filter.hash2(str1) == bloom_filter.hash2(str2))

    for i in range(10):
        for j in range(10):
            assert hashes_are_equal(strings[i], strings[j]) == ((i == j))

    # test
    for i in range(10):
        assert not bloom_filter.is_value(strings[i])

    for i in range(10):
        bloom_filter.add(strings[i])
        for j in range(10):
            assert bloom_filter.is_value(strings[j]) == (i >= j)
