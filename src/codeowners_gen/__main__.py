"""CLI entrypoint for codeowners_gen."""

from __future__ import annotations

import argparse
import json
import sys

from codeowners_gen import CodeownersError, parse_log, render, suggest_owners


def main(argv: list[str] | None = None) -> int:
    """Run CLI commands."""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="codeowners-gen",
        description="Suggest CODEOWNERS from git log numstat text.",
    )
    parser.add_argument("log_file", help="Path to git log export file, or - for stdin")
    parser.add_argument("--handles", help="Path to JSON mapping file from email to handle")
    parser.add_argument("--depth", type=int, default=1, help="Directory depth (1 to 5)")
    parser.add_argument(
        "--min-share", type=float, default=0.2, help="Minimum ownership share (0 to 1]"
    )
    parser.add_argument(
        "--max-owners", type=int, default=3, help="Maximum owners per pattern (1 to 10)"
    )

    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code != 0 else 0

    handles_map: dict[str, str] = {}
    if args.handles:
        try:
            with open(args.handles, encoding="utf-8") as hf:
                handles_map = json.load(hf)
        except (OSError, json.JSONDecodeError) as exc:
            sys.stderr.write(f"error: cannot read {args.handles}: {exc}\n")
            return 2

    try:
        if args.log_file == "-":
            content = sys.stdin.read()
        else:
            with open(args.log_file, encoding="utf-8") as lf:
                content = lf.read()
    except OSError:
        sys.stderr.write(f"error: cannot read {args.log_file}\n")
        return 2

    try:
        commits = parse_log(content)
        suggestion = suggest_owners(
            commits,
            handles=handles_map,
            depth=args.depth,
            min_share=args.min_share,
            max_owners=args.max_owners,
        )
        output = render(suggestion)
        sys.stdout.write(output)
        return 0
    except CodeownersError as exc:
        sys.stderr.write(f"error [{exc.code}]: {exc}\n")
        return 2


if __name__ == "__main__":
    sys.exit(main())
