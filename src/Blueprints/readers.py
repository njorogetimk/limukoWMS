from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from src.models import Reader, Client, Bill, db

readers = Blueprint("readers", __name__, url_prefix="/readers/v1/")


@readers.route("/<int:id>/read-meter", methods=["POST", "GET"])
@login_required
def read_meter(id):
    # Reader's id
    reader = Reader.query.get_or_404(id)
    # If not reader do nothing

    if request.method == "POST":
        client_id = request.form.get("client_id")
        current_reading = request.form.get("current_reading")

        client = Client.query.get_or_404(client_id, description="Wrong client ID")

        bill = Bill(
            current_reading=current_reading, client_id=client.id, reader_id=reader.id
        )
        db.session.add(bill)
        db.session.commit()

        return redirect(url_for("readers.read_meter", id=reader.id))

    return render_template("read_meter.html")
