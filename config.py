import os

class Config(object):
    DEBUG   = False
    TESTING = False
    CSRF_ENABLED = True
    DATABASE_URI = os.environ['DATABASE_URI']
    HOST = '0.0.0.0'
    PORT = '80'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    TESTING = True
