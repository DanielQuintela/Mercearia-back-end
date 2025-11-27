from flask import Blueprint, jsonify, request
from app.services import categories_services
from flask_jwt_extended import jwt_required
from app.schemas.categories_schema import CategoriesSchema

categories_bp = Blueprint("categories", __name__)
categories_schema = CategoriesSchema()
categories_list_schema = CategoriesSchema(many=True)

@categories_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    response = categories_services.get_categories()

    return categories_list_schema.dump(response)

@categories_bp.route("/", methods=["POST"])
@jwt_required()
def create_category():
    data = categories_schema.load(request.get_json())
    response = categories_services.create_category(data)

    return categories_schema.dump(response), 201

@categories_bp.route("/getName", methods=["GET"])
def get_by_name_route():
    paramName = request.args.get("name")

    response = categories_services.search_by_name(name= paramName)
    
    return categories_list_schema.dump(response), 200

@categories_bp.route("/<int:category_id>", methods=["PUT"])
@jwt_required()
def update(category_id):
    data = categories_schema.load(request.get_json())

    response = categories_services.update_category(id = category_id, data = data)

    return jsonify(response), 200

@categories_bp.route("/<int:category_id>", methods=["DELETE"])
@jwt_required()
def delete(category_id):

    response = categories_services.delete_category(category_id)

    return jsonify(response), 200