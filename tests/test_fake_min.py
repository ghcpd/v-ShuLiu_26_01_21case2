"""Tests for the minimal fake_useragent-style module."""

from fake_useragent_min import get_random_user_agent


def test_get_random_user_agent_returns_non_empty_string() -> None:
    """Verify get_random_user_agent returns a valid non-empty User-Agent string."""
    ua = get_random_user_agent()
    assert isinstance(ua, str)
    assert ua
    assert "Mozilla/5.0" in ua
