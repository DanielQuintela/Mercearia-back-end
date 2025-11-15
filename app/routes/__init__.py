from flask import Blueprint, jsonify
from .products_routes import products_bp
from .categories_routes import categories_bp
main_bp = Blueprint("main", __name__)


@main_bp.route("/api/v1")
def index():
    return {"message": "API da Mercearia online"}


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(categories_bp, ururl_prefix="/categories")