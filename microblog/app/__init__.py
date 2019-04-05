from flask import Flask
from app.config import Config
'''This file serves as the Flask application instance, which creates the application 
object as an instance of class Flask imported from the flask package.'''



#__name__ = a Python predefined variable that is set to the name of the module in which it is used
# __name__ is passed to Flask so that the location of the module can be used as a starting point when it
# needs to load "associated resources such as template files". So it serves as a starting place.
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
