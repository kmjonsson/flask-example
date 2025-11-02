from .github import router as github


def init(app):
    app.register_blueprint(github.api)
