from flask import jsonify
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError,
    DataError,
    OperationalError,
    ProgrammingError,
)

def handle_database_middleware(app):
    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        # roll back transaction
        from app import db
        db.session.rollback()

        return jsonify({
            "error": "Integrity error",
            "details": str(e.orig)
        }), 400

    @app.errorhandler(DataError)
    def handle_data_error(e):
        from app import db
        db.session.rollback()

        return jsonify({
            "error": "Invalid data type or value",
            "details": str(e.orig)
        }), 400

    @app.errorhandler(OperationalError)
    def handle_operational_error(e):
        return jsonify({
            "error": "Database operational error",
            "details": str(e.orig)
        }), 500

    @app.errorhandler(ProgrammingError)
    def handle_programming_error(e):
        return jsonify({
            "error": "Database programming error",
            "details": str(e.orig)
        }), 500

    @app.errorhandler(SQLAlchemyError)
    def handle_generic_sqlalchemy_error(e):
        from app import db
        db.session.rollback()

        return jsonify({
            "error": "Database error",
            "details": str(e)
        }), 500