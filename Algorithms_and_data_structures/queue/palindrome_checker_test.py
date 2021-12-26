"""Tests for palindrome checker."""


from palindrome_checker import is_palindrome

def test_is_palindrome():
    assert is_palindrome("a")
    assert is_palindrome("aa")
    assert is_palindrome("aba")
    assert is_palindrome("abba")
    assert is_palindrome("abc cba")
    assert not is_palindrome("ab c cba")
