import os
from dotenv import load_dotenv
from app.middleware.validation_erros_schemas import register_error_handlers_schema
from app.middleware.handle_global_middleware import register_error_handlers_global
from app.middleware.enforce_json_middleware import enforce_json_middleware
from app.middleware.logger import request_logger


load_dotenv()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-padrao")

    if not SECRET_KEY:
        raise ValueError("SECRET_KEY não configurada.")
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL_DEV"
    )

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
        )
        
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


def middleware_activate(app):
    register_error_handlers_schema(app)
    register_error_handlers_global(app)
    enforce_json_middleware(app)
    request_logger(app)