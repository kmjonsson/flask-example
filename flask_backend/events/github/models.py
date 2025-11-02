"""
GitHub Models
"""

from pydantic import BaseModel, ConfigDict


class GithubWebHookHook(BaseModel):
    """GitHub WebHook Hook Model"""

    id: int
    """ID of the webhook hook."""
    events: list[str]
    """List of events for the webhook hook."""

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")


class GithubWebHook(BaseModel):
    """GitHub WebHook Model"""

    hook_id: int
    """ID of the webhook."""
    hook: GithubWebHookHook
    """Details of the webhook."""

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")
