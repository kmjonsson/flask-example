# mypy: disable-error-code="no-untyped-def"
from flask_pydantic import validate

from flask_backend.api import create as create_api
from flask_backend.database import db
from flask_backend.log import log

from .crud import CrudItem
from .models import CreateItem, Item

api = create_api(__name__, "items")


@api.get("/")
@validate()
def list_item_endpoint() -> list[dict]:
    return [dict(Item.from_orm(i)) for i in CrudItem(db).list()]


@api.post("/")
@validate()
def create_item_endpoint(body: CreateItem) -> dict:
    return dict(Item.from_orm(CrudItem(db).create(body)))


@api.get("/<item_id>")
def get_item_endpoint(item_id: int) -> dict | tuple[str, int]:
    log.info(f"Fetching item with ID: {item_id}")
    item = CrudItem(db).get(item_id)
    log.info(f"Got : {item}")
    if item is None:
        return "Item not found", 404
    return dict(Item.from_orm(item))


@api.put("/<item_id>")
@validate()
def update_item_endpoint(item_id: int, body: CreateItem) -> dict | tuple[str, int]:
    item = CrudItem(db).update(item_id, body)
    if item is None:
        return "Item not found", 404

    return dict(Item.from_orm(item))


@api.delete("/<item_id>")
def delete_item_endpoint(item_id: int) -> dict | tuple[str, int]:
    item = CrudItem(db).delete(item_id)
    if item is None:
        return "Item not found", 404

    return {"detail": "Item deleted"}
