"""
Database configuration and initialization.
"""

import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Replace with your actual Database credentials
DATABASE_URL = os.environ.get("DATABASE_STRING", "sqlite:///local.db")


class Base(DeclarativeBase):
    """Base class for all ORM models."""

    pass


db = SQLAlchemy(model_class=Base)
