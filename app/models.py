from . import db
from flask_login import UserMixin

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

    def get_id(self):
        return str(self.id)

    def is_active(self):
        #  For simplicity, consider all users in table as active
        return True

    def is_authenticated(self):
        # Check if user has provided valid credentials and is currently logged in
        return 'user_id' in session and session['user_id'] == self.id