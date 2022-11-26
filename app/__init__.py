
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from app.routes.principal_router import principal_bp
from app.routes.character_router import character_bp


def create_app() -> Flask :

    app= Flask(__name__)

    app.config.from_object(Config)

    #db = SQLAlchemy(app)
    app.register_blueprint(principal_bp)
    app.register_blueprint(character_bp)

    return app