# codeowners-gen

[![CI](https://github.com/Trysac/u176-codeowners-gen/actions/workflows/ci.yml/badge.svg)](https://github.com/Trysac/u176-codeowners-gen/actions)
[![PyPI](https://img.shields.io/pypi/v/trysac-codeowners-gen.svg)](https://pypi.org/project/trysac-codeowners-gen/)

Suggest a `CODEOWNERS` file from `git log --numstat` output, weighting authors by changed lines per directory, with GitHub handle mapping and deterministic ordering.

## Why not git-fame or other tools?

While tools such as `git-fame` report authorship totals, they do not produce explicit `CODEOWNERS` rules with tunable thresholds. Teams often adopt `CODEOWNERS` late and edit it manually, resulting in inaccurate reviews. `codeowners-gen` computes directory ownership from the actual history with configurable contribution shares and directory depths.

## Installation

`pip install trysac-codeowners-gen`

## Usage Example

```python
import codeowners_gen

log = "\x1ealice@x.io\n10\t2\tsrc/app.py\n\x1ebob@x.io\n3\t0\tsrc/util.py\n"
commits = codeowners_gen.parse_log(log)
suggestion = codeowners_gen.suggest_owners(
    commits, handles={"alice@x.io": "@alice", "bob@x.io": "@bob"}, depth=1
)
print(codeowners_gen.render(suggestion))
```

## Public API Summary

- `codeowners_gen.parse_log(text: str, *, max_bytes: int = 10_000_000) -> list[Commit]`: Parses git log numstat output. Raises `CodeownersError` on malformed input or if size exceeds `max_bytes`.
- `codeowners_gen.suggest_owners(commits, *, handles=..., depth=..., min_share=..., max_owners=..., exclude=...) -> Suggestion`: Generates rules based on commit weights. Validates options (e.g., depth 1-5, min_share 0.0-1.0).
- `codeowners_gen.render(s: Suggestion) -> str`: Renders the suggestion object into the standard CODEOWNERS format.
- `CodeownersError`: Raised for parsing, input size, invalid handles, or invalid options.

See [docs/SECURITY.md](docs/SECURITY.md) for details on the security model.
