from app.extensions import db
import ulid
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func

class Audit_Log(db.Model):
    __tablename__ = "audit_log"

    id = db.Column(
        db.String(26),
        primary_key=True,
        default=lambda: str(ulid.new())
    )
    table_name = db.Column(db.String(50), nullable=False, index=True)
    db.Column(db.String(26), nullable=False, index=True)
    record_id = db.Column(db.Integer, nullable=False, index=True)
    action = db.Column(db.String(15), nullable=False)
    old_values = db.Column(JSON, nullable=False)
    new_values = db.Column(JSON, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=func.now(), nullable = False)

    def to_dict(self):
        return {
             "id": self.id,
            "table_name": self.table_name,
            "record_id": self.record_id,
            "action": self.action,
            "old_values": self.old_values,
            "new_values": self.new_values,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None
        }