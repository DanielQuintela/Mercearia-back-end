from app.extensions import db
from app.models.producers import Producers
from werkzeug.exceptions import NotFound
from app.services.audit_log_services import log_action
from app.common.enum import TableName, LogAction

def get_producers():
    return Producers.query.all()

def create_producer(data):
    producer = Producers(**data)
   
    db.session.add(producer)
    db.session.commit()

    log_action(
        table_name=TableName.PRODUCERS,
        record_id=producer.id,
        action=LogAction.CREATE,
        old_values=None,
        new_values=producer.to_dict()
    )

    return producer

def get_by_name(name):
    producer = Producers.query.filter_by(name = name).first()

    if not producer:
        raise NotFound("Producer not found")
    
    return producer

def update_producer(id, data):
    producer = Producers.query.get(id)
    if not producer:
        raise NotFound("Producer not found")

    old_values = producer.to_dict()

    if "name" in data:
        producer.name = data["name"]

    if "status" in data:
        producer.status = data["status"]

    db.session.commit()

    log_action(
        table_name=TableName.PRODUCERS,
        record_id=producer.id,
        action=LogAction.UPDATE,
        old_values=old_values,
        new_values=producer.to_dict()
    )

    return

def delete_producer(id):
    producer = Producers.query.get(id)

    if not producer:
        raise NotFound("Producer not found")
    
    old_values = producer.to_dict()

    db.session.delete(producer)
    db.session.commit()

    log_action(
        table_name=TableName.PRODUCERS,
        record_id=id,
        action=LogAction.DELETE,
        old_values=old_values,
        new_values=None
    )

    return
