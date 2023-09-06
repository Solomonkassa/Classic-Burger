from flask import Flask
from authy.api import AuthyApiClient
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from importlib import import_module
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        try:
            db.create_all()
        except Exception as e:

            print('> Error: DBMS Exception: ' + str(e) )

            # fallback to SQLite
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'tables.db')

            print('> Fallback to SQLite ')
            db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    
    # OTP_API
    app.config.from_object('apps.config')
    app.secret_key = app.config['SECRET_KEY']
    api = AuthyApiClient(app.config['AUTHY_API_KEY'])
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app