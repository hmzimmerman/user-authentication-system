# File that contains route relating to the home page

from flask import Blueprint, render_template, redirect, url_for, request, session, flash,jsonify
from flask_login import login_user, logout_user, login_required, current_user #type: ignore #? may not be needed as a way to preserve using too many libraries  #! module is installed but missing library stubs or py.typed marker
from .models import User
from .decorators import guest_only
from . import db
import time
from .auth import username_exists, email_exists  # importing something as something else is a way to avoid circular imports



views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', current_user=current_user)

@views.route('/signup', methods=['GET', 'POST'])
@guest_only
def signup():
    if request.method == 'POST':
        # Extract form data
        data = request.get_json()
        
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = data.get('username')
        email = data.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password') 
        
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        
        elif email_exists(email):
            return jsonify({'error': 'Email already exists'}), 400
            #may possibly add flash for these if jsonify isnt enough
            
        if not username:
            return jsonify({'error': 'Username is required'}), 400
        
        elif username_exists(email):
            return jsonify({'error': 'Username already exists'}), 400
            #may possibly add flash for these if jsonify isnt enough
            
        if password != confirm_password:
            flash('Passwords do not match', category='error')
        
        
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