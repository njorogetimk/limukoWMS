from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, login_required

from ..models import Admin, Reader
from ..forms import LoginForm


auth = Blueprint("auth", __name__, url_prefix="/auth/v1/")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        role = form.role.data
        password = form.password.data

        if role == "admin":
            admin = Admin.query.filter_by(username=username).first()
            if not admin or not admin.verify_password(password):
                flash("Invalid Credentials")

                return redirect(url_for("auth.login"))

            login_user(admin)

            return redirect(url_for("admin.get_admin_readers"))

        if role == "reader":
            reader = Reader.query.filter_by(username=username).first()
            if not reader or not reader.verify_password(password):
                flash("Invalid Credentials")

                return redirect(url_for("auth.login"))

            login_user(reader)

            return redirect(url_for("readers.read_meter", id=reader.id))

    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
