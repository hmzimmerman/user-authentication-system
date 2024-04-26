from flask import Flask
from flask_login import login_manager #type: ignore   #! module is installed but missing library stubs or py.typed marker 
import os
from dotenv import load_dotenv

load_dotenv() #temporary holder for variables until we decide to put them somewhere else

def create_app(templatefolder=os.getcwd()+'/templates'):
    cwd = os.getcwd()
    app = Flask(__name__, template_folder=f'{cwd}/templates')
    app.config['SECRET_KEY']: str = os.getenv('APP_CONFIG_SECRET') #acts as a way to encrypt and secure cookies/session data #? subject to removal
    
    return app


    
    
    