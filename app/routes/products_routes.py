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
    new = product_services.create_product(
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
    return jsonify(new.to_dict()), 201