import os

from flask import Flask

from config import Config
from extensions import db
from routes.api import api_bp
from routes.auth import auth_bp
from routes.errors import errors_bp
from routes.main import main_bp


def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # The SQLite database lives in instance/, which is kept separate from code.
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(errors_bp)

    # Import models before create_all so SQLAlchemy knows which tables to make.
    from models.user import User  # noqa: F401

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
