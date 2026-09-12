"""String utility functions for common text processing operations."""


def reverse(s: str) -> str:
    """Return the reverse of the input string.

    Args:
        s: The string to reverse.

    Returns:
        The reversed string.
    """
    return s[::-1]


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word in the string.

    Words are separated by spaces.

    Args:
        s: The input string.

    Returns:
        The string with each word capitalized.
    """
    return " ".join(word.capitalize() for word in s.split(" "))


def is_palindrome(s: str) -> bool:
    """Check if the string is a palindrome.

    Ignores case and non-alphanumeric characters.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Count the number of vowels (a, e, i, o, u) in the string.

    Case-insensitive.

    Args:
        s: The input string.

    Returns:
        The number of vowels.
    """
    vowels = set("aeiou")
    return sum(1 for ch in s.lower() if ch in vowels)
