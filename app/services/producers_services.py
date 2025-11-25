from app.extensions import db
from app.models.producers import Producers
from werkzeug.exceptions import NotFound

def get_producers():
    return Producers.query.all()

def create_producer(data):
    producer = Producers(**data)
   
    db.session.add(producer)
    db.session.commit()

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

    if "name" in data:
        producer.name = data["name"]

    if "status" in data:
        producer.status = data["status"]

    db.session.commit()
    return

def delete_producer(id):
    producer = Producers.query.get(id)

    if not producer:
        raise NotFound("Producer not found")
    
    db.session.delete(producer)
    db.session.commit()
    return