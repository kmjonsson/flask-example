from .items import router as items


def init(app):
    app.register_blueprint(items.api)
