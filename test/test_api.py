"""Tests for item creation and retrieval endpoints."""

from flask_backend.api import create


def test_api():
    """Test API Blueprint creation."""
    x = create(__name__, "items")
    assert x.url_prefix == "/api/v1/items"


def test_api_2():
    """Test API Blueprint creation with leading slash."""
    x = create(__name__, "/items")
    assert x.url_prefix == "/api/v1/items"
