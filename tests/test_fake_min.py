"""Tests for the minimal fake_useragent-style module."""

from fake_useragent_min import get_random_user_agent


def test_get_random_user_agent_returns_non_empty_string() -> None:
    ua = get_random_user_agent()
    assert isinstance(ua, str)
    assert ua
    assert "Mozilla/5.0" in ua
