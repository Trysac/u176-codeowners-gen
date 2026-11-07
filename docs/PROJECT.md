# Project record

## Objective

Suggest a CODEOWNERS file from git log numstat output, weighting authors by changed lines per directory, with a handle map and deterministic output.

## Scope

- Parsing git log numstat text formatted with `git log --no-merges --numstat --format=%x1e%ae`.
- Calculating directory-based ownership using specific contribution thresholds.
- Generating standard CODEOWNERS output.
- Providing a CLI wrapper around the library.

## Out of Scope

- Running git subprocesses directly (it operates on static text input).
- Validating generated rules against external GitHub Team APIs.
- Glob expansion outside of simple directory paths.
- Time-window filtering (this should be handled by `git log` flags before piping into this tool).

## Timeline

| Date | Event |
|---|---|
| 2026 | Repository created from the factory utility template. |

## Effort metrics

| Metric | Value |
|---|---|
| Tokens (input / output) | 1903751 / 17823 |
| Hours (human) | pending measurement |
| Cost (USD) | 0.3961 |

## Factory run u176 (measured from API usage)

| Phase | Model | Batch | Input | Output | Cache write | Cache read | Cost (USD) |
|---|---|---|---|---|---|---|---|
| generation | gemini-3.8-flash | yes | 4276 | 8461 | 0 | 0 | 0.0175 |
| fix-1 | gemini-3.1-flash-lite | no | 10251 | 108 | 0 | 4046 | 0.0028 |
| fix-2 | gemini-3.1-flash-lite | no | 44213 | 1568 | 0 | 122199 | 0.0165 |
| fix-3 | gemini-3.1-flash-lite | no | 53074 | 597 | 0 | 189503 | 0.0189 |
| fix-4 | gemini-3.1-flash-lite | no | 29134 | 302 | 0 | 16232 | 0.0081 |
| fix-1 | gemini-3.8-flash | no | 25735 | 291 | 0 | 41922 | 0.0235 |
| fix-2 | gemini-3.8-flash | no | 74812 | 1446 | 0 | 431993 | 0.0939 |
| fix-3 | gemini-3.8-flash | no | 46820 | 339 | 0 | 112576 | 0.0448 |
| fix-4 | gemini-3.8-flash | no | 45468 | 382 | 0 | 111814 | 0.0439 |
| fix-1 | gemini-3.8-flash | no | 10987 | 167 | 0 | 6729 | 0.0094 |
| fix-2 | gemini-3.8-flash | no | 13383 | 261 | 0 | 13505 | 0.0120 |
| fix-3 | gemini-3.8-flash | no | 11127 | 233 | 0 | 6797 | 0.0097 |
| fix-4 | gemini-3.8-flash | no | 21830 | 1043 | 0 | 16052 | 0.0215 |
| audit | gemini-3.1-flash-lite | no | 66927 | 398 | 0 | 178912 | 0.0218 |
| docs | gemini-3.1-flash-lite | no | 193434 | 2227 | 0 | 0 | 0.0517 |

Total: $0.3961. Prices: Anthropic list prices.
