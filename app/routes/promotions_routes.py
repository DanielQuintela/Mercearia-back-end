from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from app.schemas.promotions_schema import PromotionSchema
from app.services import promotions_services

promotions_bp = Blueprint("promotions", __name__)

promotion_schema = PromotionSchema()
promotion_list_schema = PromotionSchema(many=True)


@promotions_bp.route("/", methods=["GET"])
def get_promotions():
    promotions = promotions_services.get_promotions()
    return promotion_list_schema.dump(promotions), 200

@promotions_bp.route("/", methods=["POST"])
@jwt_required()
def create_promotion():
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return {"msg": "Unauthorized - Admin only"}, 403

    data = promotion_schema.load(request.get_json())
    promotion = promotions_services.create_promotion(data)

    return promotion_schema.dump(promotion), 201

@promotions_bp.route("/<int:promotion_id>", methods=["PUT"])
@jwt_required()
def update_promotion(promotion_id):
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return {"msg": "Unauthorized - Admin only"}, 403

    data = promotion_schema.load(request.get_json(), partial=True)
    updated = promotions_services.update_promotion(promotion_id, data)

    return jsonify(updated), 200

@promotions_bp.route("/<int:promotion_id>", methods=["DELETE"])
@jwt_required()
def delete_promotion(promotion_id):
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return {"msg": "Unauthorized - Admin only"}, 403

    promotions_services.delete_promotion(promotion_id)

    return jsonify({"message": "Promotion deleted successfully"}), 200


@promotions_bp.route("/<int:promotion_id>", methods=["GET"])
def get_promotion_by_id(promotion_id):
    promotion = promotions_services.get_promotion_by_id(promotion_id)
    return promotion_schema.dump(promotion), 200
