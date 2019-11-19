import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_key"
    MONGODB_SETTINGS = { 'db' : 'Ryugaku', 'host' : 'mongodb://localhost:27017/Ryugaku' }