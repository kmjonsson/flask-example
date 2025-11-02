"""
API v1
"""

from .items import api as items


def init(app):
    """Initialize the API v1 blueprint(s)."""
    app.register_blueprint(items)
