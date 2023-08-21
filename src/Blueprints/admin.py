from flask import Blueprint, render_template, request, redirect, url_for

from src.models import User, db


admin = Blueprint("admin", __name__, url_prefix="/admin/v1")


@admin.route("/users/<int:role>")
def get_users(role):
    if role == 0:
        users = User.query.all()
        return render_template("users.html", users=users, role=0)

    elif role == 1:
        users = User.query.filter_by(role=1).all()
        return render_template("users.html", users=users, role=1)

    elif role == 2:
        users = User.query.filter_by(role=2).all()
        return render_template("users.html", users=users, role=2)

    elif role == 3:
        users = User.query.filter_by(role=3).all()
        return render_template("users.html", users=users, role=3)

    else:
        return "<h1>Wrong Number</h1>"


@admin.route("/<int:admin_id>")
def get_admin(admin_id):
    return render_template("admin.html")


@admin.route("/add-user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        password1 = request.form.get("password1")

        user = User(username=username, role=role, password=password1)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("admin.get_users", role=role))

    return render_template("add_user.html")


@admin.route("/user/<int:id>")
def get_user(id):
    user = User.query.get_or_404(id)

    return render_template("user.html", user=user)


@admin.post("/delete/<int:id>")
def delete_user(id):
    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    users = User.query.all()

    return redirect(url_for("admin.get_users", role=user.role))
