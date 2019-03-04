from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Creates the application object as an instance of class Flask imported from the flask package. The __name__ variable
#  passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is
#  used. Flask uses the location of the module passed here as a starting point when it needs to load associated
# resources such as template files
app = Flask(__name__)

# Go to the package named "app" and module named "config"
app.config.from_object(Config)
# db object that represents the database
db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

# Important -
# the routes module is imported at the bottom and not at the top of the script as it is always done. The bottom
# import is a workaround to circular imports, a common problem with Flask applications. You are going to see that
# the routes module needs to import the app variable defined in this script, so putting one of the reciprocal imports
#  at the bottom avoids the error that results from the mutual references between these two files.
from app import routes, models
