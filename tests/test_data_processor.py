"""Tests for the data_processor module."""

import pytest
from src.data_processor import (
    filter_by_key,
    sort_by_key,
    aggregate_by_key,
    merge_records,
)


class TestFilterByKey:
    def test_filter_matching(self):
        data = [{"name": "Alice", "role": "admin"}, {"name": "Bob", "role": "user"}]
        assert filter_by_key(data, "role", "admin") == [{"name": "Alice", "role": "admin"}]

    def test_filter_no_match(self):
        data = [{"name": "Alice", "role": "admin"}]
        assert filter_by_key(data, "role", "moderator") == []

    def test_filter_empty_list(self):
        assert filter_by_key([], "key", "value") == []

    def test_filter_missing_key(self):
        data = [{"name": "Alice"}, {"name": "Bob"}]
        assert filter_by_key(data, "role", "admin") == []

    def test_filter_multiple_matches(self):
        data = [
            {"x": 1, "y": 2},
            {"x": 1, "y": 3},
            {"x": 2, "y": 4},
        ]
        assert filter_by_key(data, "x", 1) == [{"x": 1, "y": 2}, {"x": 1, "y": 3}]


class TestSortByKey:
    def test_sort_ascending(self):
        data = [{"name": "Charlie"}, {"name": "Alice"}, {"name": "Bob"}]
        result = sort_by_key(data, "name")
        assert result == [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]

    def test_sort_descending(self):
        data = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
        result = sort_by_key(data, "name", reverse=True)
        assert result == [{"name": "Charlie"}, {"name": "Bob"}, {"name": "Alice"}]

    def test_sort_empty_list(self):
        assert sort_by_key([], "key") == []

    def test_sort_numeric(self):
        data = [{"val": 3}, {"val": 1}, {"val": 2}]
        assert sort_by_key(data, "val") == [{"val": 1}, {"val": 2}, {"val": 3}]

    def test_sort_key_missing_raises(self):
        data = [{"a": 1}, {"b": 2}]
        with pytest.raises(KeyError):
            sort_by_key(data, "c")


class TestAggregateByKey:
    def test_aggregate_basic(self):
        data = [
            {"city": "NYC", "pop": 8},
            {"city": "LA", "pop": 4},
            {"city": "NYC", "pop": 8},
        ]
        assert aggregate_by_key(data, "city") == {"NYC": 2, "LA": 1}

    def test_aggregate_empty_list(self):
        assert aggregate_by_key([], "key") == {}

    def test_aggregate_single_item(self):
        data = [{"x": "a"}]
        assert aggregate_by_key(data, "x") == {"a": 1}

    def test_aggregate_missing_key_counts_none(self):
        data = [{"x": "a"}, {"y": "b"}]
        result = aggregate_by_key(data, "x")
        assert result == {"a": 1, None: 1}

    def test_aggregate_numeric_values(self):
        data = [{"v": 1}, {"v": 2}, {"v": 1}]
        assert aggregate_by_key(data, "v") == {1: 2, 2: 1}


class TestMergeRecords:
    def test_merge_consecutive(self):
        records = [
            {"id": 1, "a": 1},
            {"id": 1, "b": 2},
            {"id": 2, "a": 3},
        ]
        expected = [
            {"id": 1, "a": 1, "b": 2},
            {"id": 2, "a": 3},
        ]
        assert merge_records(records, "id") == expected

    def test_merge_empty_list(self):
        assert merge_records([], "key") == []

    def test_merge_single_record(self):
        records = [{"id": 1, "a": 1}]
        assert merge_records(records, "id") == [{"id": 1, "a": 1}]

    def test_merge_all_same_key(self):
        records = [
            {"id": 1, "a": 1},
            {"id": 1, "b": 2},
            {"id": 1, "c": 3},
        ]
        expected = [{"id": 1, "a": 1, "b": 2, "c": 3}]
        assert merge_records(records, "id") == expected

    def test_merge_later_overwrites_earlier(self):
        records = [
            {"id": 1, "val": "first"},
            {"id": 1, "val": "second"},
        ]
        expected = [{"id": 1, "val": "second"}]
        assert merge_records(records, "id") == expected

    def test_merge_no_consecutive_match(self):
        records = [
            {"id": 1, "a": 1},
            {"id": 2, "b": 2},
            {"id": 3, "c": 3},
        ]
        assert merge_records(records, "id") == records
