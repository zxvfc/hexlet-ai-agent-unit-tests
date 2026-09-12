# Feature: Data Processor Module

## Description
Add a new `data_processor` module that provides utilities for working with
lists of dictionaries (e.g., datasets, records).

## Functions to implement

1. **filter_by_key** - Filter a list of dicts by a key-value pair.
2. **sort_by_key** - Sort a list of dicts by a specified key.
3. **aggregate_by_key** - Count occurrences of values for a given key.
4. **merge_records** - Merge consecutive records sharing the same key value.

## Acceptance criteria

- All functions handle empty lists gracefully.
- Edge cases (missing keys, `None` values) are handled without raising unexpected exceptions.
- The module is importable and functions behave as documented.

## Status

- [x] Implementation complete (`src/data_processor.py`)
- [ ] Unit tests need to be written
