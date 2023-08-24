from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user


def permission_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can():
                flash("Please log in as an admin")
                return redirect(url_for("auth.login"))
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required()(f)
