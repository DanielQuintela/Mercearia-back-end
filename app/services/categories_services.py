from app.extensions import db
from app.models.categories import Categories
from werkzeug.exceptions import NotFound
from app.services.audit_log_services import log_action
from app.common.enum import TableName, LogAction

def get_categories():
    return Categories.query.all()

def create_category(data):
    category = Categories(**data)
   
    db.session.add(category)
    db.session.commit()

    log_action(
        table_name=TableName.CATEGORIES,
        record_id=category.id,
        action=LogAction.CREATE,
        old_values=None,
        new_values=category.to_dict()
    )

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

    old_values = category.to_dict()

    for key, value in data.items():
        if(
            hasattr(category, key) and value is not None
        ):
            setattr(category, key, value)

    db.session.commit()

    log_action(
        table_name=TableName.CATEGORIES,
        record_id=category.id,
        action=LogAction.UPDATE,
        old_values=old_values,
        new_values=category.to_dict()
    )

    return {"message": "Category updated successfully"}

def delete_category(category_id):
    category = Categories.query.get(category_id)
    if not category:
        raise NotFound("Category not found")

    old_values = category.to_dict()

    db.session.delete(category)
    db.session.commit()

    log_action(
        table_name=TableName.CATEGORIES,
        record_id=category_id,
        action=LogAction.DELETE,
        old_values=old_values,
        new_values=None
    )

    return {"response": "OK"}
