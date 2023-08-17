from flask import Flask

from src.auth import auth
from src.admin import admins
from src.clients import clients
from src.readers import readers


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    
   
    app.register_blueprint(auth)
    app.register_blueprint(admins)
    app.register_blueprint(clients)
    app.register_blueprint(readers)

    return app