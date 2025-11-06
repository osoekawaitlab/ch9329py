"""Tests for ch9329py package."""

import re

import ch9329py


def test_version() -> None:
    """Test that the version is correctly set."""
    version_pattern = r"^\d+\.\d+\.\d+$"
    assert re.match(version_pattern, ch9329py.__version__) is not None
