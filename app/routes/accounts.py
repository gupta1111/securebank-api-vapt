from flask import Blueprint, jsonify
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from app import db
from app.models.account import Account


accounts_bp = Blueprint("accounts", __name__)


# Create account
@accounts_bp.route("/create", methods=["POST"])
@jwt_required()
def create_account():
    user_id = int(get_jwt_identity())

    # Prevent duplicate account for same user
    existing_account = Account.query.filter_by(
        user_id=user_id
    ).first()

    if existing_account:
        return jsonify({
            "error": "account already exists",
            "account_id": existing_account.id,
            "account_number": existing_account.account_number
        }), 409

    account = Account(
        account_number=f"SB{user_id:06d}",
        balance=10000.0,
        user_id=user_id
    )

    db.session.add(account)
    db.session.commit()

    return jsonify({
        "message": "bank account created",
        "account_id": account.id,
        "account_number": account.account_number,
        "balance": account.balance,
        "user_id": account.user_id
    }), 201


# Get own account
@accounts_bp.route("/my-account", methods=["GET"])
@jwt_required()
def my_account():
    user_id = int(get_jwt_identity())

    account = Account.query.filter_by(
        user_id=user_id
    ).first()

    if not account:
        return jsonify({
            "error": "account not found"
        }), 404

    return jsonify({
        "account_id": account.id,
        "account_number": account.account_number,
        "balance": account.balance,
        "user_id": account.user_id
    }), 200


# Get account by ID - ownership protected
@accounts_bp.route("/<int:account_id>", methods=["GET"])
@jwt_required()
def get_account(account_id):
    user_id = int(get_jwt_identity())

    account = Account.query.filter_by(
        id=account_id,
        user_id=user_id
    ).first()

    if not account:
        return jsonify({
            "error": "account not found"
        }), 404

    return jsonify({
        "account_id": account.id,
        "account_number": account.account_number,
        "balance": account.balance,
        "user_id": account.user_id
    }), 200


# Admin-only test endpoint
@accounts_bp.route("/admin-test", methods=["GET"])
@jwt_required()
def admin_test():
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({
            "error": "admin access required"
        }), 403

    return jsonify({
        "message": "admin access granted"
    }), 200
