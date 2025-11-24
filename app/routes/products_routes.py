from flask import Blueprint, jsonify, request
from app.services import product_services
from app.schemas.products_schema import ProductSchema

products_bp = Blueprint("products", __name__)
product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)

@products_bp.route("/", methods=["GET"])
def get_products():
    products = product_services.get_products()
    return product_list_schema.dump(products)
    

@products_bp.route("/", methods=["POST"])
def create_product():
    data = product_schema.load(request.get_json())
    product = product_services.create_product(data)
    return product_schema.dump(product), 201

@products_bp.route("/<int:product_id>", methods=["PUT"])
def update(product_id):
    data = product_schema.load(request.get_json(), partial=True)

    updated_product = product_services.update_product(product_id, data)

    return jsonify(updated_product), 200

@products_bp.route("/<int:product_id>", methods=["DELETE"])
def delete(product_id):
    product_services.delete_product(product_id)
    return jsonify({"message": "Product deleted successfully"}), 200


@products_bp.route("/<int:product_id>", methods=["GET"])
def get_by_id(product_id):
    response = product_services.get_by_Id(id= product_id)
    if isinstance(response, tuple):
        body, status = response
        return jsonify(body), status
    
    return jsonify(response.to_dict()), 200
# TODO: USAR QUANDO CRIAR MIDDLEWARE
# @products_bp.route("/<int:product_id>", methods=["GET"])
# def get_by_id(product_id):
#     product = product_services.get_by_id(product_id)
#     return product_schema.dump(product), 200


@products_bp.route("/barcode", methods=["GET"])
def get_by_barcode():
    barcode = request.args.get("barcode")

    if not barcode:
        return jsonify({"error": "Barcode is required"}), 400

    product = product_services.get_product_by_barcode(barcode)
    
    return product_schema.dump(product), 200

