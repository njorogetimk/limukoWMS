from flask import Blueprint, render_template, request, redirect, url_for

from src.models import Admin, Client, Reader, Bill, db


admin = Blueprint("admin", __name__, url_prefix="/admin/v1")


@admin.route("/admin-readers")
def get_admin_readers():
    readers = Reader.query.all()
    admins = Admin.query.all()

    return render_template("admin-readers.html", readers=readers, admins=admins)


@admin.route("/clients")
def get_clients():
    clients = Client.query.all()

    return render_template("clients.html", clients=clients)


@admin.route("/client/<int:id>")
def get_client(id):
    client = Client.query.get_or_404(id)

    return render_template("client.html", client=client)


@admin.route("/add-user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        password1 = request.form.get("password1")

        if role == "admin":
            admin = Admin(username=username, password=password1)
            db.session.add(admin)
            db.session.commit()
            return redirect(url_for("admin.get_admin_readers"))

        elif role == "reader":
            reader = Reader(username=username, password=password1)
            db.session.add(reader)
            db.session.commit()
            return redirect(url_for("admin.get_admin_readers"))

        else:
            client = Client(username=username, password=password1)
            db.session.add(client)
            db.session.commit()

            return redirect(url_for("admin.get_clients"))

    return render_template("add_user.html")


@admin.post("/delete/<role>/<int:id>")
def delete_user(role, id):
    if role == "admin":
        admin = Admin.query.get_or_404(id)
        db.session.delete(admin)
        db.session.commit()

        return redirect(url_for("admin.get_admin_readers"))

    elif role == "reader":
        reader = Reader.query.get_or_404(id)
        db.session.delete(reader)
        db.session.commit()

        return redirect(url_for("admin.get_admin_readers"))

    elif role == "client":
        client = Client.query.get_or_404(id)
        db.session.delete(client)
        db.session.commit()
        return redirect(url_for("admin.get_clients"))

    else:
        return redirect(url_for("admin.get_admin_readers"))


@admin.route("/client-bills/<int:id>")
def get_client_bills(id):
    client = Client.query.get_or_404(id)
    bills = Bill.query.filter_by(client_id=id).all()

    return render_template("client_bills.html", bills=bills, client=client)
