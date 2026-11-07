# Testing

## Running

```sh
uv run pytest --cov=codeowners_gen   # tests with coverage report
uv run python scripts/check.py      # every gate, as CI and the factory run it
```

## Policy

- Branch coverage of `src/codeowners_gen` must stay at or above 80 %; the gate fails below it.
- Tests exercise the public API (`import codeowners_gen`) and assert every observable effect: return values, raised exceptions, and error codes.
- Each bug fix starts with a failing test that reproduces it.
- Tests are deterministic: no network, no wall clock, no dependence on test order.

## Layout

`tests/test_codeowners_gen.py` mirrors the public API, covering log parsing (including rename logic and binary file handling), ownership scoring logic (weighting, handle mapping, tie-breaking), and directory skipping rules. It also tests the CLI interface for file errors and stdin support.
