from flask import Blueprint, request, redirect, url_for, render_template

from src.models import Admin, Reader


auth = Blueprint("auth", __name__, url_prefix="/auth/v1/")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        password = request.form.get("password")

        if role == "admin":
            admin = Admin.query.filter_by(username=username).first()
            if not admin or password != admin.password:
                return redirect(url_for("auth.login"))

            return redirect(url_for("admin.get_admin_readers"))

        if role == "reader":
            reader = Reader.query.filter_by(username=username).first()
            if not reader or password != reader.password:
                return redirect(url_for("auth.login"))

            return redirect(url_for("readers.read_meter", id=reader.id))

    return render_template("login.html")


@auth.route("/logout")
def logout():
    return f"<h1>logout</h1>"
