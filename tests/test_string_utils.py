"""Tests for the string_utils module.

NOTE: Only reverse and capitalize_words are covered below.
The is_palindrome and count_vowels functions are NOT tested yet.
The AI agent should detect these gaps and write tests for them.
"""

import pytest
from src.string_utils import reverse, capitalize_words, is_palindrome, count_vowels


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


class TestIsPalindrome:
    def test_palindrome_simple(self):
        assert is_palindrome("racecar") is True

    def test_palindrome_mixed_case(self):
        assert is_palindrome("RaceCar") is True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_palindrome_with_punctuation(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_character(self):
        assert is_palindrome("a") is True

    def test_only_non_alphanumeric(self):
        assert is_palindrome("!!!") is True


class TestCountVowels:
    def test_count_vowels_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_count_vowels_mixed_case(self):
        assert count_vowels("AEIOU") == 5

    def test_count_vowels_no_vowels(self):
        assert count_vowels("bcdfg") == 0

    def test_count_vowels_sentence(self):
        assert count_vowels("hello world") == 3

    def test_count_vowels_empty(self):
        assert count_vowels("") == 0

    def test_count_vowels_with_numbers(self):
        assert count_vowels("h3ll0") == 0

    def test_count_vowels_y_is_not_vowel(self):
        assert count_vowels("rhythm") == 0
