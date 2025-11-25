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
    category = Categories.query.get(id)
    if not category:
        raise NotFound("Category not found")
    
    for key, value in data.items():
        if(
            hasattr(category, key) and value is not None
        ):
            setattr(category, key, value)

    db.session.commit() 

    return {"message": "Category updated successfully"}
    

def delete_category(category_id):
    category = Categories.query.get(category_id)
    if not category:
        raise NotFound("Category not found")
    
    db.session.delete(category)
    db.session.commit()
    return {"response": "OK"}