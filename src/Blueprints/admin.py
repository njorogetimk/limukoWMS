import os
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user

from src.models import Admin, Client, Reader, Bill, db
from src.decorators import admin_required
from src.forms import AddUserForm


admin = Blueprint("admin", __name__, url_prefix="/admin/v1")


@admin.route("/admin-readers")
@login_required
@admin_required
def get_admin_readers():
    readers = Reader.query.all()
    admins = Admin.query.all()
    root_id = int(os.environ.get("ADMIN_ID"))

    return render_template(
        "admin-readers.html", readers=readers, admins=admins, root_id=root_id
    )


@admin.route("/clients")
@login_required
@admin_required
def get_clients():
    clients = Client.query.all()

    return render_template("clients.html", clients=clients)


@admin.route("/client/<int:id>")
@login_required
@admin_required
def get_client(id):
    client = Client.query.get_or_404(id, description="Wrong client ID")

    return render_template("client.html", client=client)


@admin.route("/add-user", methods=["POST", "GET"])
# @login_required
# @admin_required
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

            admin = Admin(username=username)

            admin.password = password
            db.session.add(admin)
            db.session.commit()
            return redirect(url_for("admin.get_admin_readers"))

        elif role == "reader":
            check_reader = Reader.query.filter_by(username=username).first()
            if check_reader:
                flash(f"Reader username {username} taken")
                return redirect(url_for("admin.add_user"))

            reader = Reader(username=username)
            reader.password = password
            db.session.add(reader)
            db.session.commit()
            return redirect(url_for("admin.get_admin_readers"))

        else:
            check_client = Client.query.filter_by(username=username).first()
            if check_client:
                flash(f"Client username {username} taken")
                return redirect(url_for("admin.add_user"))

            client = Client(username=username)
            client.password = password
            db.session.add(client)
            db.session.commit()

            return redirect(url_for("admin.get_clients"))

    return render_template("add_user.html", form=form)


@admin.post("/delete/<role>/<int:id>")
@login_required
@admin_required
def delete_user(role, id):
    root_id = int(os.environ.get("ADMIN_ID"))
    if id == root_id:
        logout_user()
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

        return redirect(url_for("admin.get_clients"))

    else:
        flash("role does not exist")
        return redirect(url_for("admin.get_admin_readers"))


@admin.route("/client-bills/<int:id>")
@login_required
@admin_required
def get_client_bills(id):
    client = Client.query.get_or_404(id)
    bills = Bill.query.filter_by(client_id=id).all()

    return render_template("client_bills.html", bills=bills, client=client)
