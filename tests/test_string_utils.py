"""Tests for the string_utils module.

NOTE: Only reverse and capitalize_words are covered below.
The is_palindrome and count_vowels functions are NOT tested yet.
The AI agent should detect these gaps and write tests for them.
"""

import pytest
from src.string_utils import reverse, capitalize_words


class TestReverse:
    def test_reverse_simple(self):
        assert reverse("hello") == "olleh"

    def test_reverse_empty(self):
        assert reverse("") == ""

    def test_reverse_palindrome(self):
        assert reverse("racecar") == "racecar"

    def test_reverse_with_spaces(self):
        assert reverse("a b c") == "c b a"


class TestCapitalizeWords:
    def test_capitalize_simple(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_capitalize_single_word(self):
        assert capitalize_words("hello") == "Hello"

    def test_capitalize_empty(self):
        assert capitalize_words("") == ""

    def test_capitalize_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"
