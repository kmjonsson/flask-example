"""
Item Model
"""

from sqlalchemy.orm import mapped_column

from flask_backend.database import db


class Item(db.Model):
    """ORM model for an item."""

    __tablename__ = "items"
    id = mapped_column(db.Integer, primary_key=True, index=True)
    """Unique identifier for the item."""
    name = mapped_column(db.String(255), index=True)
    """Name of the item."""
    description = mapped_column(db.String(255), index=True)
    """Description of the item."""
    price = mapped_column(db.Integer)
    """Price of the item."""
