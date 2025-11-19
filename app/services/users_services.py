from app.extensions import db
from app.models.users import Users
from app.common.constants import USER_PROTECTED_FIELDS
from app.utils.encryption_password import encrypt_password

def get_users():
    return Users.query.all()

def create_user(name, email, password, role, status):
    hash_password = encrypt_password(password)

    user = Users(name=name, email=email, password=hash_password, role=role, status=status)

    db.session.add(user)
    db.session.commit()

    return user

def update_user(data):
    id = data.get("id")
    try:
        user = Users.query.get(id)

        if not user:
            return {"error": "user not found"}, 404
        
        for key, value in data.items():
            if (
                hasattr(user, key)
                and key not in USER_PROTECTED_FIELDS 
                and value is not None
            ):
                setattr(user, key, value)

        db.session.commit()
    
        return {"message": "user updated successfully"}

    except Exception as e:
        db.session.rollback() 
        
        return {"error": str(e)}, 500
    
def get_by_name(name):
    user = Users.query.filter_by(name=name).first()

    if not user:
        return {"Ok": []},
    
    return user

def get_user_by_id(data):
    id = data.get("id")
    return Users.query.get(id)

def disable_user(data):
    id = data.gey("user_id")
    user = Users.query.get(id)

    if not user:
        return {"error": "user not found"}, 404
    
    user.status = False

    db.session.commit()

    return {"message": "user disabled successfully"}, 200

def delete_user(data):
    id = data.gey("user_id")
    user = Users.query.delete(id)

    if not user:
        return {"error": "user not found"}, 404
    
    db.session.delete(user)
    db.session.commit()
    return {"response": "OK"}, 200


