from .api import app
from .api_v1 import init as init_api_v1
from .database import DATABASE_URL, db
from .events import init as init_events

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
# app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)

init_api_v1(app)
init_events(app)

with app.app_context():
    db.create_all()
