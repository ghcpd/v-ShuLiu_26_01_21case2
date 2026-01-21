"""Tests that enforce required tooling configuration for Ruff."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

try:  # Python 3.10 compatibility for TOML parsing
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - exercised only on <3.11
    import tomli as tomllib  # type: ignore[no-redef]


PYPROJECT_PATH = Path(__file__).resolve().parent.parent / "pyproject.toml"


def _load_pyproject() -> Mapping[str, Any]:
    return tomllib.loads(PYPROJECT_PATH.read_text())


def test_ruff_configuration_is_present_and_explicit() -> None:
    data = _load_pyproject()
    ruff = data.get("tool", {}).get("ruff")

    assert ruff is not None, "[tool.ruff] section must exist"
    assert ruff.get("target-version") == "py310"
    assert ruff.get("line-length") == 100
    assert ruff.get("indent-width") == 4

    include = ruff.get("include")
    assert include and {"src/**/*.py", "tests/**/*.py", "**/pyproject.toml"}.issubset(include)

    lint = ruff.get("lint")
    assert lint is not None, "[tool.ruff.lint] section must exist"

    select = lint.get("select")
    assert select and {"E", "F", "I", "UP"}.issubset(select)

    ignore = lint.get("ignore", [])
    assert "B905" in ignore

    format_cfg = ruff.get("format")
    assert format_cfg is not None, "[tool.ruff.format] section must exist"
    assert format_cfg.get("quote-style") == "double"
    assert format_cfg.get("indent-style") == "space"
