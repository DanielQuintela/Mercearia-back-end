from flask import Blueprint, jsonify, request
from app.services import product_services

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    products = product_services.get_products()
    return jsonify([p.to_dict() for p in products])

@products_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    response = product_services.create_product(
        categories_id = data.get("categories_id"),
        producer_id  = data.get("producer_id"),
        name = data.get("name"),
        barcode = data.get("barcode"),
        measure = data.get("measure"),
        weight = data.get("weight"),
        length = data.get("length"),
        image = data.get("image"),
        status = data.get("status"),
        price = data.get("price"),
    )

    return jsonify(response.to_dict()), 201

@products_bp.route("/<int:product_id>", methods=["PUT"])
def update(product_id):
    data = request.get_json()

    response = product_services.update_product(
        product_id = product_id,
        data = data
    )

    return jsonify(response), 200

@products_bp.route("/", methods=["DELETE"])
def delete():
    data = request.get_json()

    product_services.delete_product(data = data)

    return jsonify({"response": "OK"}), 200

@products_bp.route("/<int:product_id>", methods=["GET"])
def get_by_id(product_id):
    response = product_services.get_by_Id(
        id= product_id
    )
    return jsonify(response), 200

@products_bp.route("/get", methods=["GET"])
def get_by_barcode():
    data = request.get_json()

    response = product_services.get_product_by_barcode(
        data = data
    )
    return jsonify(response), 200

