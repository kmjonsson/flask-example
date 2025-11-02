from sqlalchemy.orm import mapped_column

from flask_backend.database import db


class Item(db.Model):
    __tablename__ = "items"
    id = mapped_column(db.Integer, primary_key=True, index=True)
    name = mapped_column(db.String(255), index=True)
    description = mapped_column(db.String(255), index=True)
    price = mapped_column(db.Integer)
