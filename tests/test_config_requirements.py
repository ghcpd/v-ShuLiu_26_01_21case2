"""Tests to validate that the project configuration meets prompt requirements.

These tests encode key requirements from the enhancement prompt and should:
- Fail on the baseline project (minimal Ruff config)
- Pass after the enhanced configuration is applied
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest


# Attempt to import tomllib (Python 3.11+) or fall back to tomli
try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore[import-not-found,no-redef]


@pytest.fixture
def pyproject_data() -> dict[str, Any]:
    """Load and parse pyproject.toml."""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        return tomllib.load(f)


class TestRuffConfigurationExists:
    """Verify that required Ruff configuration sections exist in pyproject.toml."""

    def test_tool_ruff_section_exists(self, pyproject_data: dict[str, Any]) -> None:
        """Verify [tool.ruff] section exists."""
        assert "tool" in pyproject_data
        assert "ruff" in pyproject_data["tool"]

    def test_tool_ruff_lint_section_exists(
        self, pyproject_data: dict[str, Any]
    ) -> None:
        """Verify [tool.ruff.lint] section exists for lint configuration."""
        ruff_config = pyproject_data["tool"]["ruff"]
        assert "lint" in ruff_config, "Missing [tool.ruff.lint] section"

    def test_tool_ruff_format_section_exists(
        self, pyproject_data: dict[str, Any]
    ) -> None:
        """Verify [tool.ruff.format] section exists for format configuration."""
        ruff_config = pyproject_data["tool"]["ruff"]
        assert "format" in ruff_config, "Missing [tool.ruff.format] section"


class TestRuffConfigurationValues:
    """Verify that Ruff configuration has appropriate values."""

    def test_target_version_is_modern_python(
        self, pyproject_data: dict[str, Any]
    ) -> None:
        """Verify target-version is set to Python 3.10 or higher."""
        ruff_config = pyproject_data["tool"]["ruff"]
        target_version = ruff_config.get("target-version", "")
        # Should be py310 or higher
        assert target_version in ("py310", "py311", "py312", "py313"), (
            f"target-version should be py310 or higher, got {target_version}"
        )

    def test_line_length_is_configured(self, pyproject_data: dict[str, Any]) -> None:
        """Verify line-length is explicitly configured."""
        ruff_config = pyproject_data["tool"]["ruff"]
        assert "line-length" in ruff_config, (
            "line-length should be explicitly configured"
        )
        line_length = ruff_config["line-length"]
        assert isinstance(line_length, int)
        assert 79 <= line_length <= 120, (
            f"line-length {line_length} is outside reasonable range"
        )

    def test_indent_width_is_configured(self, pyproject_data: dict[str, Any]) -> None:
        """Verify indent-width is explicitly configured."""
        ruff_config = pyproject_data["tool"]["ruff"]
        assert "indent-width" in ruff_config, (
            "indent-width should be explicitly configured"
        )
        assert ruff_config["indent-width"] == 4, (
            "indent-width should be 4 (Python standard)"
        )

    def test_include_patterns_cover_required_paths(
        self, pyproject_data: dict[str, Any]
    ) -> None:
        """Verify include patterns cover src, tests, and pyproject.toml."""
        ruff_config = pyproject_data["tool"]["ruff"]
        assert "include" in ruff_config, "include patterns should be specified"
        include = ruff_config["include"]

        # Convert to string for pattern matching
        include_str = str(include)
        assert "src" in include_str, "include should cover src directory"
        assert "tests" in include_str, "include should cover tests directory"
        assert "pyproject.toml" in include_str, "include should cover pyproject.toml"

    def test_lint_rules_are_selected(self, pyproject_data: dict[str, Any]) -> None:
        """Verify that lint rules are explicitly selected."""
        lint_config = pyproject_data["tool"]["ruff"]["lint"]
        assert "select" in lint_config, "lint rules should be explicitly selected"
        selected = lint_config["select"]
        assert len(selected) > 0, "At least one lint rule category should be selected"

        # Verify some essential rule categories are included
        assert "E" in selected or "F" in selected, (
            "Basic error rules (E or F) should be selected"
        )


class TestFunctionBehaviorInvariants:
    """Verify that get_random_user_agent() maintains expected behavior."""

    def test_return_type_is_string(self) -> None:
        """Verify the function returns a string."""
        from fake_useragent_min import get_random_user_agent

        result = get_random_user_agent()
        assert isinstance(result, str), "get_random_user_agent() must return a string"

    def test_return_value_is_non_empty(self) -> None:
        """Verify the function returns a non-empty string."""
        from fake_useragent_min import get_random_user_agent

        result = get_random_user_agent()
        assert len(result) > 0, "get_random_user_agent() must return a non-empty string"

    def test_return_value_contains_mozilla_prefix(self) -> None:
        """Verify the function returns a string containing Mozilla/5.0."""
        from fake_useragent_min import get_random_user_agent

        result = get_random_user_agent()
        assert "Mozilla/5.0" in result, "User-Agent string must contain 'Mozilla/5.0'"

    def test_multiple_calls_return_valid_values(self) -> None:
        """Verify multiple calls all return valid user-agent strings."""
        from fake_useragent_min import get_random_user_agent

        for _ in range(10):
            result = get_random_user_agent()
            assert isinstance(result, str)
            assert result
            assert "Mozilla/5.0" in result

    def test_function_signature_has_no_required_arguments(self) -> None:
        """Verify the function can be called without arguments."""
        import inspect

        from fake_useragent_min import get_random_user_agent

        sig = inspect.signature(get_random_user_agent)
        # All parameters should have defaults (or there should be no parameters)
        for param in sig.parameters.values():
            assert param.default is not inspect.Parameter.empty or param.kind in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            ), f"Parameter {param.name} should not be required"
