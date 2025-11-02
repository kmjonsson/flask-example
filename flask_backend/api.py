"""
Flask Backend API Initialization
"""

from flask import Blueprint, Flask

from .log import log

# Uncomment the following line to disable automatic API documentation
# app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app = Flask("flask_backend")


def create(name, base, version=1) -> Blueprint:
    """Create a Blueprint for the API.

    Args:
        name (str): The name of the Blueprint.
        base (str): The base path for the API.
        version (int, optional): The API version. Defaults to 1.

    Returns:
        Blueprint: The created Blueprint.
    """
    if base != "" and not base.startswith("/"):
        base = "/" + base
    log.info(f"Registering API v{version} with base path: {base}")
    return Blueprint(f"api_v{version}{base}", name, url_prefix=f"/api/v{version}{base}")
