"""Tests for item creation and retrieval endpoints."""

from flask_backend.api import create


def test_api():
    x = create(__name__, "items")
    assert x.url_prefix == "/api/v1/items"


def test_api_2():
    x = create(__name__, "/items")
    assert x.url_prefix == "/api/v1/items"
