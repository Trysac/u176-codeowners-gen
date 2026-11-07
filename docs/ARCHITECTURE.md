# Architecture

## Overview

`codeowners-gen` ingests git log text exports and produces deterministic `CODEOWNERS` rules.

## Core Components

1. **Parser (`parse_log`)**: 
   - Splits input on the ASCII record separator `\x1e`.
   - Parses lines in `added\tdeleted\tpath` format.
   - Handles rename syntaxes `prefix{old => new}suffix` and `old => new`.
   - Converts binary changes (`-` / `-`) to 1 added line.
   - Strictly rejects invalid input or inputs exceeding `max_bytes`.

2. **Suggestion Engine (`suggest_owners`)**:
   - Weights authors by total additions and deletions.
   - Aggregates weights for root (`*`) and directories up to specified `depth`.
   - Maps author emails to GitHub handles or team tags.
   - Filters out bot accounts (matching `[bot]` by default).
   - Evaluates share `owner_weight / total_weight >= min_share`.
   - Breaks ties deterministically by weight descending, then handle ascending.
   - Skips directories containing spaces or starting with `#`.

3. **Renderer (`render`)**:
   - Outputs standard GitHub `CODEOWNERS` syntax.
   - Emits root rule `*` first, followed by directories in ascending order (guaranteeing deeper paths override shallower parents).
