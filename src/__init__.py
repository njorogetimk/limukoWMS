import os
from flask import Flask

from src.Blueprints.auth import auth
from src.Blueprints.admin import admins
from src.Blueprints.clients import clients
from src.Blueprints.readers import readers

from src.models import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not test_config:
        app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        )
    
    else:
        app.config.from_mapping(test_config)
    
    db.app = app
    db.init_app(app)
   
    app.register_blueprint(auth)
    app.register_blueprint(admins)
    app.register_blueprint(clients)
    app.register_blueprint(readers)

    return app