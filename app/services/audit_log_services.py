from app.extensions import db
from app.models.audit_log import Audit_Log

def get_logs():
    return Audit_Log.query.all()

def log_action(table_name, record_id, action, old_values, new_values):
    audit_log = Audit_Log(
        table_name=table_name.value if hasattr(table_name, "value") else table_name,
        record_id=record_id,
        action=action.value if hasattr(action, "value") else action,
        old_values=old_values,
        new_values=new_values,
    )

    db.session.add(audit_log)
    db.session.commit()

    return audit_log

def get_logs_by_table_name(table_name):
    return Audit_Log.query.filter_by(table_name=table_name).all()

