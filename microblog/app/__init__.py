from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
'''This file serves as the Flask application instance, which creates the application 
object as an instance of class Flask imported from the flask package.'''



#__name__ = a Python predefined variable that is set to the name of the module in which it is used
# __name__ is passed to Flask so that the location of the module can be used as a starting point when it
# needs to load "associated resources such as template files". So it serves as a starting place.
app = Flask(__name__)
app.config.from_object(Config)
#SQLAlchemy is an ORM, which allows applications to manage a database using high-level entities 
#such as classes, objects, and methods into tables
db = SQLAlchemy(app)
#migrate represents the migration engine. Migrate is a wrapper for Alembic, a database migration framework for SQLAlchemy 
migrate = Migrate(app, db)

login = LoginManager(app)

mail = Mail(app)

#Flask-Bootstrap needs to be initialized like most other Flask extensions
boostrap = Bootstrap(app)

#used for when user that is not logged in tries to access a protected page
login.login_view = 'login'
from app import routes, models, errors
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost = (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr = 'no-reply@' + app.config['MAIL_SERVER'],
            toaddrs = app.config['ADMINS'], subject = 'Microblog Failure',
            credentials = auth, secure = secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
    
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes = 10240,
                                        backupCount = 10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')