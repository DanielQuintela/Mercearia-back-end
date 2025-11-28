from flask import Blueprint, jsonify, request
from app.services import producers_services
from flask_jwt_extended import jwt_required, get_jwt
from app.schemas.producers_schema import ProducersSchema

producers_bp = Blueprint("producers", __name__)
producers_schema = ProducersSchema()
producers_list_schema = ProducersSchema(many=True)

@producers_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    
    response = producers_services.get_producers()
    return producers_list_schema.dump(response)

@producers_bp.route("/", methods=["POST"])
@jwt_required()
def create_producer():
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return {"msg": "Unauthorized - Admin only"}, 403
    data = producers_schema.load(request.get_json())
    response = producers_services.create_producer(data)

    return producers_schema.dump(response), 201

@producers_bp.route("/getName", methods=["GET"])
def get_by_name():
    paramName = request.args.get("name")

    response = producers_services.get_by_name(name = paramName)

    return producers_schema.dump(response), 200
    
@producers_bp.route("/<string:producer_id>", methods=["PUT"])
@jwt_required()
def update_producers(producer_id):
    data = producers_schema.load(request.get_json(), partial= True)

    producers_services.update_producer(
        id = producer_id,
        data = data
    )

    return jsonify({"message": "producer updated successfully", "status": 200}
), 200

@producers_bp.route("/<string:producer_id>", methods=["DELETE"])
@jwt_required()
def delete(producer_id):

    producers_services.delete_producer(producer_id)

    return jsonify({"message": "producer deleted successfully", "status": 200}), 200