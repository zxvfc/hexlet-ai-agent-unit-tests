"""Data processing module for transforming and analyzing datasets.

This module was added as a new feature and currently has NO unit tests.
The AI agent should detect this gap and generate appropriate tests.
"""

from typing import Any, Dict, List


def filter_by_key(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Filter a list of dictionaries by a key-value pair.

    Args:
        data: List of dictionaries to filter.
        key: The key to check.
        value: The value to match.

    Returns:
        A new list containing only dictionaries where data[key] == value.
    """
    return [item for item in data if item.get(key) == value]


def sort_by_key(data: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """Sort a list of dictionaries by a specified key.

    Args:
        data: List of dictionaries to sort.
        key: The key to sort by.
        reverse: If True, sort in descending order.

    Returns:
        A new sorted list.

    Raises:
        KeyError: If the key is not present in all dictionaries.
    """
    return sorted(data, key=lambda item: item[key], reverse=reverse)


def aggregate_by_key(data: List[Dict[str, Any]], key: str) -> Dict[Any, int]:
    """Aggregate (count) occurrences of values for a given key.

    Args:
        data: List of dictionaries.
        key: The key to aggregate by.

    Returns:
        A dictionary mapping each unique value to its count.
    """
    result: Dict[Any, int] = {}
    for item in data:
        val = item.get(key)
        result[val] = result.get(val, 0) + 1
    return result


def merge_records(records: List[Dict[str, Any]], merge_key: str) -> List[Dict[str, Any]]:
    """Merge consecutive records that share the same merge_key value.

    When consecutive dicts have the same value for merge_key, they are
    merged into one dict with combined key-value pairs. Later keys
    overwrite earlier ones in case of conflict.

    Args:
        records: List of dictionaries to merge.
        merge_key: The key used to determine if records should be merged.

    Returns:
        A new list with merged records.
    """
    if not records:
        return []

    merged: List[Dict[str, Any]] = []
    current = dict(records[0])

    for record in records[1:]:
        if record.get(merge_key) == current.get(merge_key):
            current.update(record)
        else:
            merged.append(current)
            current = dict(record)
    merged.append(current)

    return merged
