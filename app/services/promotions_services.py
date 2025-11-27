from app.models.promotions import Promotions
from app.extensions import db
from werkzeug.exceptions import NotFound
from app.services.audit_log_services import log_action
from app.common.enum import TableName, LogAction

def get_promotions():
    return Promotions.query.all()

def create_promotion(data):
    promotion = Promotions(**data)
    db.session.add(promotion)
    db.session.commit()

    log_action(
        table_name= TableName.PROMOTIONS,
        record_id=promotion.id,
        action=LogAction.CREATE,
        old_values=None,
        new_values=promotion.to_dict()
    )
    return promotion

def update_promotion(promotion_id, data):
    promotion = Promotions.query.get(promotion_id)

    if not promotion:
        raise NotFound("Promotion not found")

    old_value = promotion.to_dict()
    for key, value in data.items():
        if value is not None and hasattr(promotion, key):
            setattr(promotion, key, value)

    db.session.commit()

    log_action(
        table_name= TableName.PROMOTIONS,
        record_id=promotion.id,
        action=LogAction.UPDATE,
        old_values=old_value,
        new_values=promotion.to_dict()
    )
    return promotion.to_dict()

def delete_promotion(promotion_id):
    promotion = Promotions.query.get(promotion_id)

    if not promotion:
        raise NotFound("Promotion not found")
    
    old_value = promotion.to_dict()
    db.session.delete(promotion)
    db.session.commit()

    log_action(
        table_name= TableName.PROMOTIONS,
        record_id=promotion.id,
        action=LogAction.DELETE,
        old_values=old_value,
        new_values=None
    )

def get_promotion_by_id(promotion_id):
    promotion = Promotions.query.get(promotion_id)

    if not promotion:
        raise NotFound("Promotion not found")

    return promotion
