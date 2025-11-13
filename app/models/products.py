from app.extensions import db
from datetime import datetime , timezone

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    categories_id = db.Column(db.Integer, db.ForeingKey("categories.id"), nullable=False)
    producer_id = db.Column(db.Integer, db.ForeignKey("producers.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    barcode = db.Column(db.String(13), nullable=False)
    measure = db.Column(db.String(50))
    weigth = db.Column(db.Float)
    length = db.Column(db.Float)
    image = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column( 
        db.DateTime, 
        default=lambda: datetime.now(timezone.utc), 
        onupdate=lambda: datetime.now(timezone.utc)
    )
    price = db.Column(db.Numeric(10, 2))
    
    categories = db.relationship("Category", backref = "products")
    producer = db.relationship("Producer", backref = "products")

    def to_dict(self):
        return {
            "id": self.id,
            "categories_id": self.categories_id,
            "producer_id": self.producer_id,
            "name": self.name,
            "barcode": self.barcode,
            "measure": self.measure,
            "weight": self.weight,
            "length": self.length,
            "image": self.image,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "price": str(self.price)
        }
