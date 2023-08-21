from flask import Blueprint


clients = Blueprint('clients', __name__, url_prefix='/clients/v1/')

@clients.route('/')
def get_clients():
    return '<h1>All Clients</h1>'

@clients.route('/client/<int:client_id>')
def get_client(client_id):

    return f'<h1>Client {client_id}</h1>'
