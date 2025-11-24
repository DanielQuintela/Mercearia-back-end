from flask import request, jsonify

def enforce_json_middleware(app):
    @app.before_request
    def ensure_json():
        if request.method in ["POST", "PUT", "PATCH"]:
            if not request.is_json:
                return jsonify({"error": "Request must be JSON"}), 400


