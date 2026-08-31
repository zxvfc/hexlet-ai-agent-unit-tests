# AGENTS.md

## Commands

- **Install**: `pip install -e ".[dev]"`
- **Run tests**: `pytest tests/ -v`
- **Check coverage**: `pytest tests/ --cov=src --cov-report=term-missing`
- No linter or type checker is configured.

## Test conventions

- One `class` per function (e.g., `class TestAdd`, `class TestFilterByKey`)
- Import from `src.*` package: `from src.calculator import add`
- Float comparisons: `pytest.approx()`
- Error cases: `pytest.raises(ExceptionType, match="message")`
- Test file naming: `tests/test_{module}.py`

## Structure

- `src/` — source modules (calculator, string_utils, data_processor, geometry)
- `tests/` — pytest test files, one per module
- `features/` — feature specs (markdown)

## Notes

- This is a demo for AI-agent test generation. Some test gaps are intentional.
- README.md's coverage table is stale — the test gaps it lists are all filled.
- CI workflow (`.github/workflows/ai-test-agent.yml`) auto-generates tests on PRs via opencode.
