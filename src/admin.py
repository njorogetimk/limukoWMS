from flask import Blueprint


admins = Blueprint('admins', __name__, url_prefix='/admins/v1')

@admins.route('/')
def get_admins():
    return '<h1>All Admins</h1>'

@admins.route('/admin/<int:admin_id>')
def get_admin(admin_id):

    return f'<h1>admin {admin_id}</h1>'

@admins.route('/add-admin')
def add_admin():
    
    return f'<h1>Add admin</h1>'

@admins.route('/modify-admin/<int:admin_id>')
def modify_admin(admin_id):

    return f'<h1>Modify admin</h1>'


@admins.route('/delete-admin/<int:admin_id>')
def delete_admin(admin_id):

    return f'<h1>Delete admin</h1>'