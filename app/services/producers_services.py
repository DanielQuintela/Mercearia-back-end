from app.extensions import db
from app.models.producers import Producers

def get_producers():
    return Producers.query.all()

def create_producer(name, status):
    producer = Producers(name=name, status=status)
   
    db.session.add(producer)
    db.session.commit()

    return producer

def get_by_name(name):
    producer = Producers.query.filter_by(name = name).first()
    if not producer:
        return {"error": "Producer not found"}, 404
    return producer

def update_producer(id, data):

    try:
        producer = Producers.query.get(id)
        if not producer:
            return {"error": "producer not found"}, 404

        if "name" in data:
            producer.name = data["name"]

        if "status" in data:
            producer.status = data["status"]

        db.session.commit()
        return {"message": "producer updated successfully"}, 200

    except Exception as e:
        db.session.rollback() 
        
        return {"error": str(e)}, 500

def delete_producer(id):
    producer = Producers.query.get(id)

    if producer == None:
        return {"error": "producer not found"}, 404
    
    db.session.delete(producer)
    db.session.commit()
    return {"message": "producer deleted successfully"}, 200