import os
from flask import Flask, redirect, url_for, render_template
from flask_login import LoginManager

from src.Blueprints.auth import auth
from src.Blueprints.admin import admin
from src.Blueprints.readers import readers

from src.models import db, Admin, Reader


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if not test_config:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )

    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(readers)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        if str(user_id)[0] == "1":
            return Admin.query.get(int(user_id))
        if str(user_id)[0] == "2":
            return Reader.query.get(int(user_id))

    @app.route("/")
    def main():
        return render_template("index.html")

    return app
