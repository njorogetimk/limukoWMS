import os
from flask import Flask, render_template
from flask_login import LoginManager
from dotenv import load_dotenv

from .Blueprints import auth, admin, readers, client

from src.models import db, Admin, Reader, AnonymousUser


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    load_dotenv()
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.app = app
    db.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(readers)
    app.register_blueprint(client)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        if str(user_id)[0] == "1":
            return Admin.query.get(int(user_id))
        if str(user_id)[0] == "2":
            return Reader.query.get(int(user_id))

    login_manager.anonymous_user = AnonymousUser

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html", error=e), 404

    @app.route("/")
    def main():
        return render_template("index.html")

    return app
