from flask import Blueprint, render_template


admin = Blueprint("admin", __name__, url_prefix="/admin/v1")


@admin.route("/")
def get_admins():
    return render_template("admin.html")


@admin.route("/admin/<int:admin_id>")
def get_admin(admin_id):
    return render_template("admin.html")


@admin.route("/add-admin")
def add_admin():
    return f"<h1>Add admin</h1>"


@admin.route("/modify-admin/<int:admin_id>")
def modify_admin(admin_id):
    return f"<h1>Modify admin</h1>"


@admin.route("/delete-admin/<int:admin_id>")
def delete_admin(admin_id):
    return f"<h1>Delete admin</h1>"


# Add modify and delete clients
@admin.route("/add-client")
def add_client():
    return f"<h1>Add Client</h1>"


@admin.route("/modify-client/<int:client_id>")
def modify_client(client_id):
    return f"<h1>Modify Client</h1>"


@admin.route("/delete-client/<int:client_id>")
def delete_client(client_id):
    return f"<h1>Delete Client</h1>"


# Add Edit and delete meter readers
@admin.route("/add-reader")
def add_reader():
    return f"<h1>Add reader</h1>"


@admin.route("/modify-reader/<int:reader_id>")
def modify_reader(reader_id):
    return f"<h1>Modify reader</h1>"


@admin.route("/delete-reader/<int:reader_id>")
def delete_reader(reader_id):
    return f"<h1>Delete reader</h1>"
