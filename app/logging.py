import logging
import sys
import json
import os
from datetime import datetime


class JSONFormatter(logging.Formatter):
    """Format logs as JSON for production"""
    
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
            
        return json.dumps(log_data)


def setup_logging(app):
    """Configure logging based on environment"""
    log_level = app.config.get('LOG_LEVEL', 'INFO')
    flask_env = app.config.get('FLASK_ENV', 'development')
    
    # Remove existing handlers
    app.logger.handlers.clear()
    
    # Create console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(getattr(logging, log_level))
    
    # Use JSON formatter for production, text for dev/staging
    if flask_env == 'production':
        formatter = JSONFormatter()
    else:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(getattr(logging, log_level))
    
    app.logger.info(f"Logging configured: env={flask_env}, level={log_level}")