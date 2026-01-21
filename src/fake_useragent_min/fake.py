"""Minimal subset of fake-useragent-style functionality.

This module provides a tiny example that can be formatted and linted with ruff.
"""

from __future__ import annotations

import random
from collections.abc import Sequence


_USER_AGENTS: Sequence[str] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
)


def get_random_user_agent() -> str:
    """Return a random user-agent string from a small built-in list."""
    return random.choice(_USER_AGENTS)
