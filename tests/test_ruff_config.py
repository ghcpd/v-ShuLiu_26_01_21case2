"""Tests to validate Ruff configuration requirements.

These tests verify that the pyproject.toml contains the expected Ruff
configuration sections and settings as required by the project specification.
These tests should fail on the baseline project and pass after the enhanced
configuration is applied.
"""

from __future__ import annotations

from pathlib import Path

import pytest

# Path to the pyproject.toml relative to the tests directory
PYPROJECT_PATH = Path(__file__).parent.parent / "pyproject.toml"


@pytest.fixture
def pyproject_content() -> str:
    """Load the pyproject.toml content."""
    return PYPROJECT_PATH.read_text(encoding="utf-8")


class TestRuffConfigurationSections:
    """Test that required Ruff configuration sections exist in pyproject.toml."""

    def test_tool_ruff_section_exists(self, pyproject_content: str) -> None:
        """Verify [tool.ruff] section exists."""
        assert "[tool.ruff]" in pyproject_content

    def test_tool_ruff_lint_section_exists(self, pyproject_content: str) -> None:
        """Verify [tool.ruff.lint] section exists for modern Ruff config style."""
        assert "[tool.ruff.lint]" in pyproject_content

    def test_tool_ruff_format_section_exists(self, pyproject_content: str) -> None:
        """Verify [tool.ruff.format] section exists for formatting configuration."""
        assert "[tool.ruff.format]" in pyproject_content


class TestRuffConfigurationValues:
    """Test that required Ruff configuration values are properly set."""

    def test_target_version_is_configured(self, pyproject_content: str) -> None:
        """Verify target-version is set to a modern Python version (3.10+)."""
        assert "target-version" in pyproject_content
        # Should target Python 3.10 or higher
        assert any(
            f'target-version = "py3{v}"' in pyproject_content for v in range(10, 15)
        )

    def test_line_length_is_configured(self, pyproject_content: str) -> None:
        """Verify line-length is explicitly configured."""
        assert "line-length" in pyproject_content

    def test_indent_width_is_configured(self, pyproject_content: str) -> None:
        """Verify indent-width is explicitly configured."""
        assert "indent-width" in pyproject_content

    def test_include_patterns_configured(self, pyproject_content: str) -> None:
        """Verify include patterns target source, tests, and pyproject.toml."""
        assert "include" in pyproject_content
        # Check that source and tests directories are included
        assert "src/**/*.py" in pyproject_content
        assert "tests/*.py" in pyproject_content
        assert "**/pyproject.toml" in pyproject_content

    def test_lint_select_rules_configured(self, pyproject_content: str) -> None:
        """Verify that lint rules are explicitly selected."""
        assert "select" in pyproject_content
        # Should include at least pycodestyle (E), Pyflakes (F), and isort (I)
        assert '"E"' in pyproject_content or "'E'" in pyproject_content
        assert '"F"' in pyproject_content or "'F'" in pyproject_content
        assert '"I"' in pyproject_content or "'I'" in pyproject_content


class TestFunctionalBehaviorPreserved:
    """Test that the functional behavior of get_random_user_agent is preserved."""

    def test_function_returns_string(self) -> None:
        """Verify get_random_user_agent returns a string type."""
        from fake_useragent_min import get_random_user_agent

        result = get_random_user_agent()
        assert isinstance(result, str)

    def test_function_returns_non_empty_string(self) -> None:
        """Verify get_random_user_agent returns a non-empty string."""
        from fake_useragent_min import get_random_user_agent

        result = get_random_user_agent()
        assert len(result) > 0

    def test_function_returns_mozilla_user_agent(self) -> None:
        """Verify all returned values contain Mozilla/5.0 prefix."""
        from fake_useragent_min import get_random_user_agent

        # Call multiple times to increase confidence
        for _ in range(10):
            result = get_random_user_agent()
            assert "Mozilla/5.0" in result

    def test_function_is_callable_without_arguments(self) -> None:
        """Verify get_random_user_agent can be called with no arguments."""
        from fake_useragent_min import get_random_user_agent

        # This should not raise any exception
        _ = get_random_user_agent()

    def test_function_signature_unchanged(self) -> None:
        """Verify the function signature has no required parameters."""
        import inspect

        from fake_useragent_min import get_random_user_agent

        sig = inspect.signature(get_random_user_agent)
        # Should have no required parameters
        required_params = [
            p
            for p in sig.parameters.values()
            if p.default is inspect.Parameter.empty
            and p.kind
            not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)
        ]
        assert len(required_params) == 0

    def test_return_type_annotation_is_str(self) -> None:
        """Verify the function has str return type annotation."""
        import inspect

        from fake_useragent_min import get_random_user_agent

        sig = inspect.signature(get_random_user_agent)
        assert sig.return_annotation is str or sig.return_annotation == "str"
