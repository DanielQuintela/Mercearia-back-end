from app.extensions import db
from sqlalchemy import text

def health_check():
    try:
        db.session.execute(text("SELECT 1"))
        return {
            "status": "Ok",
            "database": "connected"
        }, 200
    
    except Exception as e:
        return {
            "status": "error",
            "database": "unavailable",
            "details": str(e)
        }, 500
