from flask import Blueprint, render_template
from flask_login import login_required

from src.models import Client
from src.decorators import adred_required


client = Blueprint("client", __name__, url_prefix="/client/v1")


@client.route("/clients")
@login_required
@adred_required
def get_clients():
    clients = Client.query.all()

    return render_template("clients.html", clients=clients)


@client.route("/client/<int:id>")
@login_required
@adred_required
def get_client(id):
    client = Client.query.get_or_404(id, description="Wrong client ID")

    return render_template("client.html", client=client)
