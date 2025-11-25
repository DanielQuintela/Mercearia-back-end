from flask import Blueprint, jsonify, request
from app.services import users_services
from app.schemas.users_schema import UsersSchema, UserResponseSchema

users_bp = Blueprint("users", __name__)
users_schema = UsersSchema()
users_list_schema = UserResponseSchema(many=True)
users_response_schema = UserResponseSchema()

@users_bp.route("/", methods=["GET"])
def get_all():
    response = users_services.get_users()

    return users_list_schema.dump(response)

@users_bp.route("/", methods=["POST"])
def create_user():
    data = users_schema.load(request.get_json())

    response = users_services.create_user(data)

    return users_response_schema.dump(response), 201
    
@users_bp.route("/", methods=["PUT"])
def update_user():
    data = users_schema.load(request.get_json())

    response = users_services.update_user(data)

    return jsonify(response)

@users_bp.route("/getByName", methods=["GET"])
def get_by_name():
    name = request.args.get("user_name")

    response = users_services.get_by_name(name)

    return users_list_schema.dump(response), 200

# TODO: PAREI AQUI
@users_bp.route("/get", methods=["GET"])
def get_by_id():
    name = request.args.get("user_id")

    response = users_services.get_user_by_id(name)

    return jsonify(response.to_dict())

@users_bp.route("/disableUser", methods=["PUT"])
def disable_user():
    data = users_schema.load(request.get_json())

    response = users_services.disable_user(data)

    return jsonify(response)

@users_bp.route("/", methods=["DELETE"])
def delete_user():
    data = users_schema.load(request.get_json())


    response = users_services.delete_user(data)

    return jsonify(response)

# TODO: TESTES DE HASH
@users_bp.route("/check", methods=["GET"])
def check():
    data = users_schema.load(request.get_json())

    response = users_services.check(data)
    return jsonify(response)