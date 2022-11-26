
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from app.routes.principal_router import principal_bp


def create_app() -> Flask :

    app= Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(principal_bp)
    #db = SQLAlchemy(app)

    return app