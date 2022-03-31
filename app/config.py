from os import environ as env

class Config:
    
    URI = env.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = env.get('SECRET_KEY')
    PORT = int(env.get('PORT', 5000))