from app.extensions import db
from app.models.products import Product
from app.common.constants import PRODUCT_PROTECTED_FIELDS

def get_products():
    return Product.query.all()

def create_product(categories_id, producer_id , name , barcode, 
                    measure, weight, length , image, status, price ):
    
    new = Product(categories_id = categories_id, producer_id = producer_id, name = name,
                    barcode = barcode, measure = measure, weight = weight, length = length,
                    image = image, status = status, price = price)
    db.session.add(new)
    db.session.commit()
    return new

def get_by_Id(id):
    return Product.query.get(id)

def update_product(id, **data):
    product = Product.query.get(id)
    if not product:
        return {"error": "Product not found"}, 404
    
    for key, value in data.items():
        if (
            hasattr(product, key)
            and key not in PRODUCT_PROTECTED_FIELDS 
            and value is not None
        ):
            setattr(product, key, value)

    db.session.commit()
    
    return {"message": "Product updated successfully"}
  
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return None
    db.session.delete(product)
    db.session.commit()
    return True

def get_product_by_barcode(barcode):
    barcode = barcode.strip()
    product = Product.query.filter_by(barcode = barcode).first()
    return product
