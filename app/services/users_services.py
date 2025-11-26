from app.extensions import db
from app.models.users import Users
from app.common.constants import USER_PROTECTED_FIELDS
from app.utils.encryption_password import encrypt_password, verify_password
from werkzeug.exceptions import NotFound
from app.services.audit_log_services import log_action
from app.common.enum import TableName, LogAction

def get_users():
    return Users.query.all()

def create_user(data):
    hash_password = encrypt_password(data["password"])

    user = Users(
        name=data["name"],
        email=data["email"],
        password=hash_password,
        status=data.get("status", True)
    )

    db.session.add(user)
    db.session.commit()

    log_action(
        table_name=TableName.USERS,
        record_id=user.id,
        action=LogAction.CREATE,
        old_values=None,
        new_values=user.to_dict()
    )

    return user

def update_user(data, user_id):
    # TODO: REFATORAR QUANDO CRIAR JWT

    user = Users.query.get(user_id)

    if not user:
        raise NotFound("User not found")

    old_values = user.to_dict()

    for key, value in data.items():
        if (
            hasattr(user, key)
            and key not in USER_PROTECTED_FIELDS
            and value is not None
        ):
            setattr(user, key, value)

    db.session.commit()

    log_action(
        table_name=TableName.USERS,
        record_id=user.id,
        action=LogAction.UPDATE,
        old_values=old_values,
        new_values=user.to_dict()
    )

    return {"message": "user updated successfully"}

def get_by_name(name):

    user = Users.query.filter(Users.name.ilike(f"%{name}%")).all()
    
    return user

def get_user_by_id(id):
    user = Users.query.get(id)
    if not user:
        raise NotFound("User not found")
    return user

def disable_user(user_id):
    user = Users.query.get(user_id)

    if not user:
        raise NotFound("User not found")

    old_values = user.to_dict()

    user.status = False
    db.session.commit()

    log_action(
        table_name=TableName.USERS,
        record_id=user.id,
        action=LogAction.UPDATE,
        old_values=old_values,
        new_values=user.to_dict()
    )

    return

def delete_user(user_id):
    user = Users.query.get(user_id)
    if not user:
        raise NotFound("User not found")

    old_values = user.to_dict()

    db.session.delete(user)
    db.session.commit()

    log_action(
        table_name=TableName.USERS,
        record_id=user_id,
        action=LogAction.DELETE,
        old_values=old_values,
        new_values=None
    )

    return

def check(data, user_id):
    password = data.get("password")

    user = Users.query.get(user_id)

    if not user:
        return False

    print("---------------")
    print(user.password)
    # Verificar senha
    return verify_password(user.password, password)

def create_adm(data):
    hash_password = encrypt_password(data["password"])

    adm = Users(
        name=data["name"],
        email=data["email"],
        password=hash_password,
        role=data.get("role", "admin"),
        status=data.get("status", True)
    )

    db.session.add(adm)
    db.session.commit()

    log_action(
        table_name=TableName.USERS,
        record_id=adm.id,
        action=LogAction.CREATE,
        old_values=None,
        new_values=adm.to_dict()
    )

    return adm
