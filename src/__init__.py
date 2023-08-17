from flask import Flask

from src.Blueprints.auth import auth
from src.Blueprints.admin import admins
from src.Blueprints.clients import clients
from src.Blueprints.readers import readers


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    
   
    app.register_blueprint(auth)
    app.register_blueprint(admins)
    app.register_blueprint(clients)
    app.register_blueprint(readers)

    return app