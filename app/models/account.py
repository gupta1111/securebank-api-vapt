from app import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    account_number = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    balance = db.Column(
        db.Float,
        default=10000.0,
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )
