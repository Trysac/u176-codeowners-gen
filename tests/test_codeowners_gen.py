"""Behavior tests for the public API of codeowners_gen."""

from __future__ import annotations

import pytest

import codeowners_gen


def test_normalize_trims_and_lowercases() -> None:
    assert codeowners_gen.normalize("  Hello World ") == "hello world"


@pytest.mark.parametrize("value", ["", "   ", "\t\n"])
def test_normalize_rejects_blank_input(value: str) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        codeowners_gen.normalize(value)


def test_version_is_semver() -> None:
    parts = codeowners_gen.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
