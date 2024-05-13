# File that contains route relating to the home page

from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from flask_login import login_user, logout_user, login_required, current_user #type: ignore #? may not be needed as a way to preserve using too many libraries  #! module is installed but missing library stubs or py.typed marker
from .models import User
from .decorators import guest_only
from . import db
import time
from .auth import UserAuth as Auth # importing something as something else is a way to avoid circular imports


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', current_user=current_user)

@views.route('/signup', methods=['GET', 'POST'])
@guest_only
def signup():
    if request.method == 'POST':
        # Extract form data
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
        
        # Create a new user
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password_hash=password, password_salt=password, secret_key=password, is_two_factor_enabled=False) #todo remove password salt, secret key, and tfa from variables once nullable error is solved

        # Add new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Login the new user
        login_user(new_user) 
        flash('Welcome', category='success') 
        time.sleep(2)
        return redirect(url_for('views.home'))
    
    return render_template('signup.html')

@views.route('/login', methods=['GET', 'POST'])
@guest_only
def login():
    if request.method == 'POST':
        # Extract form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Query user from the database
        user = User.query.filter_by(username=username).first()

        # Check if user exists and password hash matches
        if user and user.password_hash == password:
            flash('Login successful', category='success')
            session['user_id'] = user.id  # Set session cookie
            login_user(user)
            return redirect(url_for('views.home'))
        else:
            flash('Invalid username or password', category='error')
            return redirect(url_for('views.login'))
    
    return render_template('login.html')

@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))