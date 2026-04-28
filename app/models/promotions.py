from app.extensions import db
import ulid
from sqlalchemy.sql import func

class Promotions(db.Model):
    __tablename__ = "promotions"

    id = db.Column(db.String(26), primary_key=True, default=lambda: str(ulid.new()))
    name = db.Column(db.String(50), nullable=False, unique=True)
    status = db.Column(db.Boolean, default=True)
    starts_at = db.Column(db.DateTime, nullable=False)
    ends_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "starts_at": self.starts_at.isoformat() if self.starts_at else None,
            "ends_at": self.ends_at.isoformat() if self.ends_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
