import os

import pytest

os.environ["DATABASE_STRING"] = "sqlite:///./test.db"


@pytest.fixture()
def client(test_db):
    from flask_backend import app

    return app.test_client()


@pytest.fixture()
def test_db():
    from flask_backend import app
    from flask_backend.database import db

    with app.app_context():
        db.create_all()
    yield
    with app.app_context():
        db.drop_all()
