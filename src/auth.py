from flask import Blueprint


auth = Blueprint('auth', __name__, url_prefix='/auth/v1/')


@auth.route('/login')
def login():

    return f'<h1>Logged in</h1>'

@auth.route('/logout')
def logout():

    return f'<h1>logout</h1>'