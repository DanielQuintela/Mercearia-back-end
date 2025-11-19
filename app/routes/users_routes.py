from flask import Blueprint, jsonify, request
from app.services import users_services

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def get_all():
    response = users_services.get_users()

    return jsonify([p.to_dict() for p in response])

@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    response = users_services.create_user(
        name = data.get("name"),
        email = data.get("email"),
        password = data.get("password"),
        role = data.get("role"),
        status = data.get("status")
    )

    return jsonify(response.to_dict()), 201
    
@users_bp.route("/", methods=["PUT"])
def update_user():
    data = request.get_json()

    response = users_services.update_user(data)

    return jsonify(response)

@users_bp.route("/getByName/<string:user_name>", methods=["GET"])
def get_by_name(user_name):
    response = users_services.get_by_name(user_name)

    return jsonify(response.to_dict())

@users_bp.route("/get", methods=["GET"])
def get_by_id():
    data = request.get_json()
    response = users_services.get_user_by_id(data)

    return jsonify(response.to_dict())

@users_bp.route("/disableUser", methods=["PUT"])
def disable_user():
    data = request.get_json()

    response = users_services.disable_user(data)

    return jsonify(response)

@users_bp.route("/", methods=["DELETE"])
def delete_user():
    data = request.get_json()

    response = users_services.delete_user(data)

    return jsonify(response)

# TODO: TESTES DE HASH
@users_bp.route("/check", methods=["GET"])
def check():
    data = request.get_json()
    response = users_services.check(data)
    return jsonify(response)