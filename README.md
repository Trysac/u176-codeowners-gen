# codeowners-gen

[![PyPI version](https://img.shields.io/pypi/v/trysac-codeowners-gen)](https://pypi.org/project/trysac-codeowners-gen/)
[![License: MIT](https://img.shields.io/pypi/l/trysac-codeowners-gen)](LICENSE)
[![CI](https://github.com/Trysac/u176-codeowners-gen/actions/workflows/ci.yml/badge.svg)](https://github.com/Trysac/u176-codeowners-gen/actions/workflows/ci.yml)

Suggest a CODEOWNERS file from git log numstat output, weighting authors by changed lines per directory, with a handle map and deterministic output

## Problem

Describe in two or three sentences the concrete problem this utility solves, who hits it, and what
they do today without it. Replace this paragraph when the first real feature lands.

## Install

```sh
pip install trysac-codeowners-gen
# or
uv add trysac-codeowners-gen
```

Requires Python 3.10 or newer. No runtime dependencies.

## Usage

```python
import codeowners_gen

# normalize() trims surrounding whitespace and lower-cases the text.
print(codeowners_gen.normalize("  Hello World "))  # -> "hello world"

# Blank input is rejected explicitly instead of returning an empty string.
try:
    codeowners_gen.normalize("   ")
except ValueError as exc:
    print(f"rejected: {exc}")
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md) and [decisions](docs/decisions/)
- [Testing](docs/TESTING.md) and [security](docs/SECURITY.md)
- [Project record](docs/PROJECT.md) and [stack](docs/STACK.md)
- [Changelog](CHANGELOG.md) and [contributing guide](CONTRIBUTING.md)

## License

[MIT](LICENSE) (c) 2026 Miguel Gomez
