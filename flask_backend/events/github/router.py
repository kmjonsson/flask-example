"""
GitHub Events Router
"""

from flask import Blueprint
from flask_pydantic import validate  # mypy: disable-error-code="no-untyped-def"

from flask_backend.log import log

from .models import GithubWebHook

api = Blueprint("events/github", __name__, url_prefix="/events/github")


@api.post("/")
@validate()
def github_event_endpoint(body: GithubWebHook) -> GithubWebHook:
    """Endpoint to receive GitHub events via webhooks."""
    log.info(f"Received GitHub event: {body.hook.events}")
    return body
