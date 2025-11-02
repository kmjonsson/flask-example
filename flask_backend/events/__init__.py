"""
Events
"""

from .github import api as github


def init(app):
    """Initialize the events blueprint(s)."""
    app.register_blueprint(github)
