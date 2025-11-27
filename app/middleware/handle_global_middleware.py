from flask import jsonify
from werkzeug.exceptions import HTTPException, Unauthorized
from .database_middleware import handle_database_middleware

def register_error_handlers_global(app):

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return jsonify({
            "status": e.code,        
            "error": e.name,         
            "message": e.description
        }), e.code
    
    handle_database_middleware(app)

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):

        if hasattr(e, "messages"):
            return jsonify({
                "status": 400,
                "error": "Validation Error",
                "message": e.messages
            }), 400

        print(f"[ERROR] {type(e).__name__}: {str(e)}")

        return jsonify({
            "status": 500,
            "error": "Internal Server Error",
            "message": "An unexpected error occurred"
        }), 500
    
    @app.errorhandler(Unauthorized)
    def handle_unauthorized(e):
        return jsonify({"error": e.description, "status": e.code}), 401
