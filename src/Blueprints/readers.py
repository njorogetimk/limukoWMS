from flask import Blueprint

readers = Blueprint('readers', __name__, url_prefix='/readers/v1/')


@readers.route('/')
def get_readers():
    return '<h1>All readers</h1>'

@readers.route('/reader/<int:reader_id>')
def get_reader(reader_id):

    return f'<h1>reader {reader_id}</h1>'

@readers.route('/read-meter')
def read_meter():
    return f'<h1>Read Meter</h1>'