from flask import Blueprint, request, jsonify
from .services import authenticate

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.post("")
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    
    result = authenticate(email, password)
    return jsonify(result, {"status": 200}), 200
