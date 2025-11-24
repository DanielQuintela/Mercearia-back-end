from marshmallow import ValidationError
from flask import jsonify

def register_error_handlers_schema(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({
            "errors": err.messages,
            "message": "Invalid data sent"
        }), 400
