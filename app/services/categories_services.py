from app.extensions import db
from app.models.categories import Categories
from werkzeug.exceptions import NotFound

def get_categories():
    return Categories.query.all()

def create_category(data):
    category = Categories(**data)
   
    db.session.add(category)
    db.session.commit()

    return category

def search_by_name(name):
    category = Categories.query.filter(Categories.name.ilike(f"%{name}%")).all()
    if not category:
        raise NotFound("Category not found")
    return category

def update_category(id, data):

    try:
        category = Categories.query.get(id)
        if not category:
            raise NotFound("Category not found")
        
        if "name" in data:
            category.name = data["name"]
        
        if "status" in data:
            category.status = data["status"]

        db.session.commit() 

        return {"message": "Category updated successfully"}, 200
    
    except Exception as e:
            db.session.rollback() 
            
            return {"error": str(e)}, 500

def delete_category(id):
    category = Categories.query.get(id)
    if not category:
        return {"error": "Category not found"}, 404
    
    db.session.delete(category)
    db.session.commit()
    return {"response": "OK"}, 200