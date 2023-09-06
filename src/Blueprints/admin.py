import os
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from ..models import Admin, Client, Reader, db
from ..decorators import admin_required
from ..forms import AddUserForm


admin = Blueprint("admin", __name__, url_prefix="/admin/v1")


@admin.route("/admin-readers")
@login_required
@admin_required
def get_admin_readers():
    readers = Reader.query.all()
    admins = Admin.query.all()
    root_id = os.environ.get("ROOT_ID")

    return render_template(
        "admin-readers.html", readers=readers, admins=admins, root_id=int(root_id)
    )


@admin.route("/reader/<int:id>")
@login_required
@admin_required
def get_reader(id):
    reader = Reader.query.get_or_404(id)
    return render_template("reader.html", reader=reader)


@admin.route("/add-user", methods=["POST", "GET"])
@login_required
@admin_required
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        username = form.username.data
        role = form.role.data
        password = form.password.data

        if role == "admin":
            check_admin = Admin.query.filter_by(username=username).first()
            if check_admin:
                flash(f"Admin username {username} taken")
                return redirect(url_for("admin.add_user"))

            pasw_hash = generate_password_hash(password)

            admin = Admin(username=username, password_hash=pasw_hash)
            db.session.add(admin)
            db.session.commit()
            return redirect(url_for("admin.get_admin_readers"))

        elif role == "reader":
            check_reader = Reader.query.filter_by(username=username).first()
            if check_reader:
                flash(f"Reader username {username} taken")
                return redirect(url_for("admin.add_user"))

            pasw_hash = generate_password_hash(password)

            reader = Reader(username=username, password_hash=pasw_hash)
            db.session.add(reader)
            db.session.commit()
            return redirect(url_for("admin.get_admin_readers"))

        else:
            check_client = Client.query.filter_by(username=username).first()
            if check_client:
                flash(f"Client username {username} taken")
                return redirect(url_for("admin.add_user"))

            pasw_hash = generate_password_hash(password)

            client = Client(username=username, password_hash=pasw_hash)
            db.session.add(client)
            db.session.commit()

            return redirect(url_for("client.get_clients"))

    return render_template("add_user.html", form=form)


@admin.post("/delete/<role>/<int:id>")
@login_required
@admin_required
def delete_user(role, id):
    root_id = os.environ.get("ROOT_ID")
    if current_user.get_id() != root_id:
        flash("Not allowed! Sorry")
        return redirect(url_for("main"))
    if role == "admin":
        admin = Admin.query.get_or_404(id, description="Wrong administrator ID")
        db.session.delete(admin)
        db.session.commit()
        flash(f"{admin.username} successfully deleted!")

        return redirect(url_for("admin.get_admin_readers"))

    elif role == "reader":
        reader = Reader.query.get_or_404(id, description="Wrong reader ID")
        db.session.delete(reader)
        db.session.commit()
        flash(f"{reader.username} successfully deleted!")

        return redirect(url_for("admin.get_admin_readers"))

    elif role == "client":
        client = Client.query.get_or_404(id, description="Wrong client ID")
        db.session.delete(client)
        db.session.commit()
        flash(f"{client.username} successfully deleted!")

        return redirect(url_for("client.get_clients"))

    else:
        flash("role does not exist")
        return redirect(url_for("admin.get_admin_readers"))
