import logging
from flask import Flask
from config import Config

def create_app():
    """
    Factory function to create and configure the Flask app.
    Includes logging, config loading, and blueprint registration.
    """
    # Create Flask app
    app = Flask(__name__)
    app.config.from_object(Config)  # Load settings from config.py

    # -----------------------------
    # Logging setup
    # -----------------------------
    # Log to a file inside container
    file_handler = logging.FileHandler("flask.log")
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    app.logger.addHandler(file_handler)

    # Also log to console (stdout) for Docker logs
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(file_formatter)
    app.logger.addHandler(stream_handler)

    app.logger.info("Flask app created")

    # -----------------------------
    # Register blueprints
    # -----------------------------
    from .routes import main  # your blueprint in routes.py
    app.register_blueprint(main)

    return app
