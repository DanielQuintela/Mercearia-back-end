from app.models.users import Users
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import Unauthorized
from app.utils.encryption_password import verify_password
from app.routes.users_routes import users_response_schema

def authenticate(email, password):
    user = Users.query.filter_by(email=email).first()

    if not user:
        raise Unauthorized("Invalid credentials")
    
    if not verify_password(hashed=user.password, password=password):
        raise Unauthorized("Invalid credentials")

    token = create_access_token(identity=str(user.id),
                                additional_claims={"role": user.role, "name": user.name})

    return {"access_token": token, "user": users_response_schema.dump(user)}
