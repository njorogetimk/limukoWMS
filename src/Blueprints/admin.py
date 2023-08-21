from flask import Blueprint


admins = Blueprint("admins", __name__, url_prefix="/admins/v1")


@admins.route("/")
def get_admins():
    return "<h1>All Admins</h1>"


@admins.route("/admin/<int:admin_id>")
def get_admin(admin_id):
    return f"<h1>admin {admin_id}</h1>"


@admins.route("/add-admin")
def add_admin():
    return f"<h1>Add admin</h1>"


@admins.route("/modify-admin/<int:admin_id>")
def modify_admin(admin_id):
    return f"<h1>Modify admin</h1>"


@admins.route("/delete-admin/<int:admin_id>")
def delete_admin(admin_id):
    return f"<h1>Delete admin</h1>"


# Add modify and delete clients
@admins.route("/add-client")
def add_client():
    return f"<h1>Add Client</h1>"


@admins.route("/modify-client/<int:client_id>")
def modify_client(client_id):
    return f"<h1>Modify Client</h1>"


@admins.route("/delete-client/<int:client_id>")
def delete_client(client_id):
    return f"<h1>Delete Client</h1>"


# Add Edit and delete meter readers
@admins.route("/add-reader")
def add_reader():
    return f"<h1>Add reader</h1>"


@admins.route("/modify-reader/<int:reader_id>")
def modify_reader(reader_id):
    return f"<h1>Modify reader</h1>"


@admins.route("/delete-reader/<int:reader_id>")
def delete_reader(reader_id):
    return f"<h1>Delete reader</h1>"
