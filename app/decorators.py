from flask import redirect, url_for
from flask_login import current_user
from functools import wraps

def guest_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('views.home'))
        return f(*args, **kwargs)
    return decorated_function