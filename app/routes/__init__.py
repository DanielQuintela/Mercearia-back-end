from flask import Blueprint, jsonify
from .products_routes import products_bp
from .categories_routes import categories_bp
from .producers_routes import producers_bp
from app.services import health_services
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return {"message": "API da Mercearia online"}


def register_blueprints(app):
    app.register_blueprint(main_bp, url_prefix="/api/v1")
    app.register_blueprint(products_bp, url_prefix="/api/v1/products")
    app.register_blueprint(categories_bp, url_prefix="/api/v1/categories")
    app.register_blueprint(producers_bp, url_prefix="/api/v1/producers")

@main_bp.route("/health", methods=["GET"])
def health_check():
    return health_services.health_check()