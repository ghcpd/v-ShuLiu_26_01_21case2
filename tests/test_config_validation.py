"""Tests to validate project configuration and requirements."""

from __future__ import annotations

from pathlib import Path

import tomllib

from fake_useragent_min import get_random_user_agent


def test_pyproject_has_ruff_configuration() -> None:
    """Verify that pyproject.toml has proper ruff configuration sections."""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"

    with pyproject_path.open("rb") as f:
        config = tomllib.load(f)

    # Check that ruff tool section exists
    assert "tool" in config
    assert "ruff" in config["tool"]

    ruff_config = config["tool"]["ruff"]

    # Check required configuration values
    assert "target-version" in ruff_config
    assert ruff_config["target-version"] == "py310"

    assert "line-length" in ruff_config
    assert isinstance(ruff_config["line-length"], int)

    assert "indent-width" in ruff_config
    assert ruff_config["indent-width"] == 4

    # Check include patterns
    assert "include" in ruff_config
    includes = ruff_config["include"]
    assert "src/**/*.py" in includes
    assert "tests/**/*.py" in includes
    assert "**/pyproject.toml" in includes


def test_pyproject_has_ruff_lint_configuration() -> None:
    """Verify that pyproject.toml has ruff lint configuration."""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"

    with pyproject_path.open("rb") as f:
        config = tomllib.load(f)

    # Check that ruff.lint section exists
    assert "tool" in config
    assert "ruff" in config["tool"]
    assert "lint" in config["tool"]["ruff"]

    lint_config = config["tool"]["ruff"]["lint"]

    # Check that select rules are defined
    assert "select" in lint_config
    assert isinstance(lint_config["select"], list)
    assert len(lint_config["select"]) > 0


def test_get_random_user_agent_behavior_invariants() -> None:
    """Test that get_random_user_agent maintains its contract."""
    # Generate multiple user agents to check consistency
    user_agents = [get_random_user_agent() for _ in range(10)]

    for ua in user_agents:
        # Must be a string
        assert isinstance(ua, str)

        # Must be non-empty
        assert len(ua) > 0

        # Must contain Mozilla/5.0 as per specification
        assert "Mozilla/5.0" in ua

        # Must be from a known list (validate it's deterministic)
        assert any(expected in ua for expected in ["Windows NT", "Macintosh", "Linux"])


def test_get_random_user_agent_returns_different_values() -> None:
    """Verify that get_random_user_agent can return different values."""
    # Generate many samples to have high probability of seeing variation
    user_agents = {get_random_user_agent() for _ in range(50)}

    # Should have more than one unique value (randomness check)
    # With 50 samples from 3 options, probability of all same is negligible
    assert len(user_agents) > 1
