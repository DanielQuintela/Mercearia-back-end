from flask import Blueprint, jsonify, request
from app.services import producers_services

producers_bp = Blueprint("producers", __name__)

@producers_bp.route("/", methods=["GET"])
def get_all():
    response = producers_services.get_producers()

    return jsonify([p.to_dict() for p in response])

@producers_bp.route("/", methods=["POST"])
def create_producer():
    data = request.get_json()
    response = producers_services.create_producer(
        name = data.get("name"),
        status = data.get("status")
    )

    return jsonify(response.to_dict()), 201

@producers_bp.route("/getName", methods=["GET"])
def get_by_name():
    paramName = request.args.get("name")

    response = producers_services.get_by_name(
        name = paramName
    )

    if isinstance(response, tuple):
        body, status = response
        return jsonify(body), status
    
    return jsonify(response.to_dict()), 200
    
@producers_bp.route("/<int:producer_id>", methods=["PUT"])
def update(producer_id):
    data = request.get_json()

    response = producers_services.update_producer(
        id = producer_id,
        data = data
    )

    return jsonify(response), 200

@producers_bp.route("/", methods=["DELETE"])
def delete():
    data = request.get_json()

    producer_id = data.get("producer_id")
    response, status = producers_services.delete_producer(producer_id)

    return jsonify(response), status