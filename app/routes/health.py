from flask import Blueprint, jsonify
from sqlalchemy import text
from app.db import SessionContext

bp = Blueprint("health", __name__)

@bp.route("/health", methods=["GET"])
def health():
    try:
        with SessionContext() as session:
            session.execute(text("SELECT 1"))
        
        return jsonify({
            "status": "healthy", 
        }), 200

    except Exception as e:
        print(f"Health check failed: {e}")
        return jsonify({
            "status": "unhealthy", 
            "database": "disconnected", 
            "error": "Database not connected please check you connection"
        }), 503