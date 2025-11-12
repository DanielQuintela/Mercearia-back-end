from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return {"message": "API da Mercearia online"}


def register_blueprints(app):
    app.register_blueprint(main_bp)
    # app.register_blueprint(produtos_bp, url_prefix="/produtos")