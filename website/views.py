# File that contains route relating to the home page

from flask import Blueprint, render_template
from flask_login import login_required, current_user #type: ignore #? may not be needed as a way to preserve using too many libraries  #! module is installed but missing library stubs or py.typed marker

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/login')
def login():
    return render_template('login.html')