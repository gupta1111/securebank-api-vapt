from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.models.account import Account

accounts_bp = Blueprint("accounts", __name__)


@accounts_bp.route("/create", methods=["POST"])
@jwt_required()
def create_account():
    user_id = int(get_jwt_identity())

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
        "account_number": account.account_number
    }), 201


@accounts_bp.route("/my-account", methods=["GET"])
@jwt_required()
def my_account():
    user_id = int(get_jwt_identity())

    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({
            "error": "account not found"
        }), 404

    return jsonify({
        "account_id": account.id,
        "account_number": account.account_number,
        "balance": account.balance
    }), 200
