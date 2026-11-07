# Deterministic directory ownership scoring and rename resolution

Status: accepted (generated, pending human review)

## Context

Generating CODEOWNERS from git history requires converting raw numstat output into directory-level ownership patterns while accounting for file renames, binary files, bot accounts, and tie-breaking.

## Decision

Use an in-memory two-pass model: first parse git log numstat text into typed immutable records resolving rename patterns; then aggregate line change weights per directory up to configurable depth and sort matching owners by descending contribution and ascending string handle.

## Consequences

Zero runtime dependencies, completely deterministic output, protection against unbounded input sizes and malformed records.
