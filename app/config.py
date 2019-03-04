import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# The Flask-SQLAlchemy extension takes the location of the application's database
# from the SQLALCHEMY_DATABASE_URI configuration variable.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tomdata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False