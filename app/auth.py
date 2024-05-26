import re
from .models import User as USER
from . import app


def email_exists(email):
   return USER.session.query(USER.exists().where(USER.email == email)).scalar()

def username_exists(username): #prefunction to test route 
   return USER.session.query(USER.exists().where(USER.username == username)).scalar()
      
      
   


