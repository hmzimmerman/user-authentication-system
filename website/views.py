# File that contains route relating to the home page

from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import login_required, current_user #type: ignore #? may not be needed as a way to preserve using too many libraries  #! module is installed but missing library stubs or py.typed marker
from .models import User
from . import db
import time
from .auth import UserAuth as Auth # importing something as something else is a way to avoid circular imports


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password') 
        

        #todo add function in auth to check for if email, or username is registered in db most will be added into the auth class but idk if you want to add data functions into their own classification
        #in the meantime ill add code as if theyre there in a block
        '''
        email_exists = function call
        username_exists = function call
        valid email = function call 
        
        if email exist:
            flash('Email already associated with account', category='error') #flash just acts as a mini popup
        elif not valid email:
            flash('invalid email address', category='error')
        elif username_exists:
            flash('Username is unavailable', category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
            
        password = salt_password(password)
        password = hash_password(password)
        
        '''
        
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password_hash=password, password_salt=password, secret_key=password,is_two_factor_enabled=True) #todo remove password salt, secret key, and tfa from variables once nullable error is solved
        #todo add new user to db and commit it, flash, login success, then log them in and redirect them to homepage
        db.session.add(new_user)
        db.session.commit()
        flash('Welcome', category='success') 
        time.sleep(2)
        #login_user() 
        return redirect(url_for('views.home'))
    
    return render_template('signup.html')

@views.route('/login')
def login():
    return render_template('login.html')




@views.route('/signout')
def signout():
    ...