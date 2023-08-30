from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user


def permission_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_admininistrator():
                flash("Please log in as an admin")
                return redirect(url_for("auth.login"))
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def office_required():
    """
    Both admins and readers
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_adred():
                flash("Please log in as an admin or reader")
                return redirect(url_for("auth.login"))
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def reader_required():
    """
    Both admins and readers
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_red():
                flash("Please log in as a reader")
                return redirect(url_for("auth.login"))
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required()(f)


def adred_required(f):
    return office_required()(f)


def red_required(f):
    return reader_required()(f)
