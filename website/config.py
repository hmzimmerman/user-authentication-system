import os

class Config:
    SECRET_KEY = os.getenv('APP_CONFIG_SECRET', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://localhost/userauthenticationsystem')
    SQLALCHEMY_TRACK_MODIFICATIONS = False