from app.extensions import db
from datetime import datetime , timezone

class Audit_Log(db.Model):
    __tablename__ = "audit_log"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    record_id = db.Column(db.Integer, nullable=False)
    action = db.Column(db.String(15), nullable=False)
    old_values = db.Column(db.String(120), nullable=False)
    new_values = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable = False)

    def to_dict(self):
        return {
             "id": self.id,
            "name": self.name,
            "record_id": self.record_id,
            "action": self.action,
            "old_values": self.old_values,
            "new_values": self.new_values,
            "timestamp": self.created_at.isoformat() if self.created_at else None
        }