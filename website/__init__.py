from flask import Flask
from flask_login import LoginManager #type: ignore   #! module is installed but missing library stubs or py.typed marker 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .config import Config
import os

load_dotenv() #temporary holder for variables until we decide to put them somewhere else

db = SQLAlchemy()

def create_app(templatefolder=f'{os.getcwd()}/templates'):
    
    app = Flask(__name__, template_folder=templatefolder)
    app.config.from_object(Config) #acts as a way to encrypt and secure cookies/session data #? subject to removal

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import and register blueprints
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app