from flask import request, jsonify


def enforce_json_middleware(app):
    @app.before_request
    def ensure_json():
        if request.method in ["POST", "PUT", "PATCH"]:
            if "application/json" not in request.headers.get("Content-Type", ""):
                return jsonify({"error": "Content-Type must be application/json"}), 400


