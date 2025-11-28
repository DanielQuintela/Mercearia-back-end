from app.extensions import db
import ulid
from sqlalchemy.sql import func

class Producers(db.Model):
    __tablename__ = "producers"

    id = db.Column(db.String(26), primary_key=True, default=lambda: str(ulid.new()))
    name = db.Column(db.String(50), nullable=False, unique=True)
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable = False)
    updated_at = db.Column( 
        db.DateTime, 
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable = False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }