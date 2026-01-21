"""Minimal fake_useragent-like package used for tooling examples.

This package provides a simple `get_random_user_agent()` function
that returns a random User-Agent string from a built-in list.
"""

from .fake import get_random_user_agent

__all__ = ["get_random_user_agent"]
