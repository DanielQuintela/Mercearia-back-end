from app.extensions import db
from app.models.products import Product
from app.common.constants import PRODUCT_PROTECTED_FIELDS
from werkzeug.exceptions import NotFound
from app.services.audit_log_services import log_action
from app.common.enum import TableName, LogAction

def get_products():
    return Product.query.all()

def create_product(data):
    new = Product(**data)
    db.session.add(new)
    db.session.commit()

    log_action(
        table_name= TableName.PRODUCTS,
        record_id=new.id,
        action=LogAction.CREATE,
        old_values=None,
        new_values=new.to_dict()
    )
    return new

def get_by_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    return product

def update_product(product_id, data):
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    
    old_values = product.to_dict()

    for key, value in data.items():
        if (
            hasattr(product, key)
            and key not in PRODUCT_PROTECTED_FIELDS
            and value is not None
        ):
            setattr(product, key, value)

    db.session.commit()

    log_action(
        table_name=TableName.PRODUCTS,
        record_id=product.id,
        action=LogAction.UPDATE,
        old_values=old_values,
        new_values=product.to_dict()
    )

    return {"message": "Product updated successfully"}

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        raise NotFound("Product not found")
    
    old_values = product.to_dict()

    db.session.delete(product)
    db.session.commit()

    log_action(
        table_name=TableName.PRODUCTS,
        record_id=product.id,
        action=LogAction.DELETE,
        old_values=old_values,
        new_values=None
    )

    return {"message": "Product deleted successfully"}

def get_product_by_barcode(barcode):
    return Product.query.filter_by(barcode=barcode).first()
