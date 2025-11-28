from app.extensions import db
from sqlalchemy.sql import func
from datetime import datetime , timezone
import ulid

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(26), primary_key=True, default=lambda: str(ulid.new()))
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(30), nullable=False, default="user")
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable = False)
    updated_at = db.Column( 
        db.DateTime, 
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }