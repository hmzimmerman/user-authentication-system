from flask import Flask
from flask_login import LoginManager #type: ignore   #! module is installed but missing library stubs or py.typed marker 
import os
from dotenv import load_dotenv

load_dotenv() #temporary holder for variables until we decide to put them somewhere else

def create_app(templatefolder=f'{os.getcwd()}/templates'):
    
    app = Flask(__name__, template_folder=templatefolder)
    app.config['SECRET_KEY'] = os.getenv('APP_CONFIG_SECRET') #acts as a way to encrypt and secure cookies/session data #? subject to removal
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app


    
    
    