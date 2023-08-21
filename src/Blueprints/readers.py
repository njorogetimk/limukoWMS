from flask import Blueprint

readers = Blueprint("readers", __name__, url_prefix="/readers/v1/")


@readers.route("/read-meter")
def read_meter():
    return f"<h1>Read Meter</h1>"
