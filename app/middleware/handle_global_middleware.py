from flask import jsonify
from werkzeug.exceptions import HTTPException, NotFound, BadRequest

def register_error_handlers(app):
    
    @app.errorhandler(HTTPException)
    def handle_http_exceptions(e):
        return jsonify({"error": e.description}), e.code


    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        if hasattr(e, "messages"):
            return jsonify({"error": e.messages}), 400

        print(f"[ERROR] {type(e).__name__}: {e}")

        return jsonify({"error": "Internal server error"}), 500
