from app.extensions import db
from app.models.products import Product

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


