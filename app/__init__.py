from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    @app.after_request
    def add_security_headers(response):
     response.headers["X-Content-Type-Options"] = "nosniff"
     response.headers["X-Frame-Options"] = "DENY"
     response.headers["Content-Security-Policy"] = "default-src 'self'"
     return response

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///securebank.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "dev-secret-change-later"

    db.init_app(app)
    jwt.init_app(app)

    from app.models.user import User
    from app.models.account import Account
    from app.routes.auth import auth_bp
    from app.routes.accounts import accounts_bp

    app.register_blueprint(
        auth_bp,
        url_prefix="/api/auth"
    )

    app.register_blueprint(
        accounts_bp,
        url_prefix="/api/accounts"
    )

    with app.app_context():
        db.create_all()

    return app
