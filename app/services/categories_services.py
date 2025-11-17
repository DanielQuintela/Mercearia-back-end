from app.extensions import db
from app.models.categories import Categories

def get_categories():
    return Categories.query.all()

def create_category(name, status):
    category = Categories(name=name, status=status)
   
    db.session.add(category)
    db.session.commit()

    return category

def get_by_name(name):
    category = Categories.query.filter_by(name = name).first()
    if not category:
        return {"error": "Category not found"}, 404
    return category

def update_category(id, data):

    try:
        category = Categories.query.get(id)
        print(category)
        if not category:
            return {"error": "Category not found"}, 404
        
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
    return 200