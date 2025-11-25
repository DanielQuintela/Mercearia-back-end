from flask import Blueprint, jsonify, request
from app.services import users_services
from app.schemas.users_schema import UsersSchema, UserResponseSchema

users_bp = Blueprint("users", __name__)
users_schema = UsersSchema()
users_list_schema = UserResponseSchema(many=True)
users_response_schema = UserResponseSchema()

# @users_bp.route("/", methods=["GET"])
# def get_all():
#     response = users_services.get_users()

#     return users_list_schema.dump(response)
# TODO: REMOVER ROTA DE TESTE E DEIXAR A DE CIMA
@users_bp.route("/", methods=["GET"])
def get_all():
    response = users_services.get_users()

    return users_list_schema.dump(response)


@users_bp.route("/", methods=["POST"])
def create_user():
    data = users_schema.load(request.get_json())

    response = users_services.create_user(data)

    return users_response_schema.dump(response), 201
    
@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = users_schema.load(request.get_json())

    response = users_services.update_user(data, user_id)

    return jsonify(response)

@users_bp.route("/getByName", methods=["GET"])
def get_by_name():
    name = request.args.get("user_name")

    response = users_services.get_by_name(name)

    return users_list_schema.dump(response), 200

@users_bp.route("/get", methods=["GET"])
def get_by_id():
    id = request.args.get("user_id")

    response = users_services.get_user_by_id(id)

    return users_response_schema.dump(response), 200

@users_bp.route("/disableUser/<int:user_id>", methods=["PUT"])
def disable_user(user_id):
    users_services.disable_user(user_id)

    return jsonify({"message": "user disabled successfully", "status": 200}), 200

# TODO: PAREI AQUI
@users_bp.route("/", methods=["DELETE"])
def delete_user():
    data = users_schema.load(request.get_json())


    response = users_services.delete_user(data)

    return jsonify(response)

# TODO: TESTES DE HASH
@users_bp.route("/check/<int:user_id>", methods=["GET"])
def check(user_id):
    data = users_schema.load(request.get_json(), partial=True)

    response = users_services.check(data, user_id)
    return jsonify(response)

@users_bp.route("/createAdm", methods=["POST"])
def create_new_adm():
    data = users_schema.load(request.get_json())

    response = users_services.create_adm(data)

    return users_response_schema.dump(response)