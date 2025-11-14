from flask import Flask
from .config import ProductionConfig, DevelopmentConfig
from .extensions import db, migrate, ma
from .routes import register_blueprints
import os

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    # TODO: PARA QUANDO EU FOR IMPLEMENTAR OS SCHEMAS
    # ma.init_app(app)

    register_blueprints(app)

    print(f"[*] Flask iniciado no ambiente: {env}")

    return app