"""
Items API
"""

# mypy: disable-error-code="no-untyped-def"
from flask_pydantic import validate

from flask_backend.api import create as create_api
from flask_backend.database import db

from .crud import CrudItem
from .models import CreateItem, Item

api = create_api(__name__, "items")


@api.get("/")
@validate()
def list_item_endpoint() -> list[dict]:
    """List all items.
    Returns:
        list[dict]: A list of all items.
    """
    return [dict(Item.from_orm(i)) for i in CrudItem(db).list()]


@api.post("/")
@validate()
def create_item_endpoint(body: CreateItem) -> dict:
    """Create a new item.
    Args:
        body (CreateItem): The item data to create.
    Returns:
        dict: The created item data.
    """
    return dict(Item.from_orm(CrudItem(db).create(body)))


@api.get("/<item_id>")
def get_item_endpoint(item_id: int) -> dict | tuple[str, int]:
    """Get an item by its ID.

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        dict: The item data if found.
    """
    item = CrudItem(db).get(item_id)
    if item is None:
        return "Item not found", 404
    return dict(Item.from_orm(item))


@api.put("/<item_id>")
@validate()
def update_item_endpoint(item_id: int, body: CreateItem) -> dict | tuple[str, int]:
    """Update an item by its ID.
    Args:
        item_id (int): The ID of the item to update.
        body (CreateItem): The updated item data.
    Returns:
        dict: The updated item data.
    """
    item = CrudItem(db).update(item_id, body)
    if item is None:
        return "Item not found", 404

    return dict(Item.from_orm(item))


@api.delete("/<item_id>")
def delete_item_endpoint(item_id: int) -> dict | tuple[str, int]:
    """Delete an item by its ID.
    Args:
        item_id (int): The ID of the item to delete.
    Returns:
        dict: A confirmation message if the item was deleted.
    """
    item = CrudItem(db).delete(item_id)
    if item is None:
        return "Item not found", 404

    return {"detail": "Item deleted"}
