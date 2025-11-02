"""
GitHub Models
"""

from pydantic import BaseModel, ConfigDict


class GithubWebHookHook(BaseModel):
    """GitHub WebHook Hook Model"""

    id: int
    events: list[str]

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")


class GithubWebHook(BaseModel):
    """GitHub WebHook Model"""

    hook_id: int
    hook: GithubWebHookHook

    # Ignore extra fields in the incoming JSON payload
    model_config = ConfigDict(extra="ignore")
