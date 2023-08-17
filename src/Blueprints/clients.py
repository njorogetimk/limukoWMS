from flask import Blueprint


clients = Blueprint('clients', __name__, url_prefix='/clients/v1/')

@clients.route('/')
def get_clients():
    return '<h1>All Clients</h1>'

@clients.route('/client/<int:client_id>')
def get_client(client_id):

    return f'<h1>Client {client_id}</h1>'

@clients.route('/add-client')
def add_client():
    
    return f'<h1>Add Client</h1>'

@clients.route('/modify-client/<int:client_id>')
def modify_client(client_id):

    return f'<h1>Modify Client</h1>'


@clients.route('/delete-client/<int:client_id>')
def delete_client(client_id):

    return f'<h1>Delete Client</h1>'