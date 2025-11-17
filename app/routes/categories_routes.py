from flask import Blueprint, jsonify, request
from app.services import categories_services

categories_bp = Blueprint("categories", __name__)

@categories_bp.route("/", methods=["GET"])
def get_all():
    response = categories_services.get_categories()

    return jsonify([p.to_dict() for p in response])

@categories_bp.route("/", methods=["POST"])
def create_category():
    data = request.get_json()
    response = categories_services.create_category(
        name = data.get("name"),
        status = data.get("status")
    )

    return jsonify(response.to_dict()), 201

@categories_bp.route("/getName", methods=["GET"])
def get_by_name_route():
    paramName = request.args.get("name")

    response = categories_services.get_by_name(
        name= paramName
    )
    
    if isinstance(response, tuple):
        body, status = response
        return jsonify(body), status

    return jsonify(response.to_dict()), 200
    
@categories_bp.route("/<int:category_id>", methods=["PUT"])
def update(category_id):
    data = request.get_json()

    response = categories_services.update_category(
        id = category_id,
        data = data
    )

    return jsonify(response), 200

@categories_bp.route("/", methods=["DELETE"])
def delete():
    data = request.get_json()

    category_id = data.get("category_id")
    categories_services.delete_category(category_id)

    return jsonify({"response": "OK"}), 200