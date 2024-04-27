from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    password_salt = db.Column(db.String(100), nullable=False)
    secret_key = db.Column(db.String(100), nullable=False)
    is_two_factor_enabled = db.Column(db.Boolean, nullable=False, default=False)