from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
import os
import json

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///securebank.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv(
        "JWT_SECRET_KEY",
        "securebank-development-secret"
    )

    @app.after_request
    def add_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"

        if request.path.startswith("/docs"):
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; "
                "script-src 'self' 'unsafe-inline'; "
                "style-src 'self' 'unsafe-inline'; "
                "img-src 'self' data:; "
                "font-src 'self' data:"
            )
        else:
            response.headers["Content-Security-Policy"] = "default-src 'self'"

        return response

    db.init_app(app)
    jwt.init_app(app)

    from app.models.user import User
    from app.models.account import Account
    from app.routes.auth import auth_bp
    from app.routes.accounts import accounts_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(accounts_bp, url_prefix="/api/accounts")

    with app.app_context():
        db.create_all()

    @app.route("/docs/swagger.json")
    def swagger_json():
        swagger_path = os.path.join(
            app.root_path,
            "..",
            "docs",
            "swagger.json"
        )

        with open(swagger_path, "r") as f:
            return json.load(f)

    SWAGGER_URL = "/docs"
    API_URL = "/docs/swagger.json"

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            "app_name": "SecureBank API"
        }
    )

    app.register_blueprint(
        swaggerui_blueprint,
        url_prefix=SWAGGER_URL
    )

    return app
