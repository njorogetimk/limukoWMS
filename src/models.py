import random
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, AnonymousUserMixin


db = SQLAlchemy()


class Admin(UserMixin, db.Model):
    """
    This holds the administrator table definition

    Attributes
    ----------
    username: str
        unique username of the admin
    password_hash: str
        hashed password

    Methods
    ----------
    is_administrator()
        checks if the user is an admin
    is_adred()
        checks if user is either an admin or reader
    is_red()
        checks if user is a reader
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username: str, password_hash: str) -> None:
        """
        Parameters
        ---------
        username: str
            the username
        password_hash: str
            the hashed password
        id: int
            id initialized randomly whith a 1 at the start
        """
        self.id = int("1" + str(random.random())[2:10])
        self.username = username
        self.password_hash = password_hash

    @property
    def password(self):
        raise AttributeError("Password is Read Only!")

    def is_administrator(self) -> bool:
        """
        Checks if is an administrator
        """
        return True

    def is_adred(self) -> bool:
        """
        Checks if is either an administrator or reader
        """
        return True

    def is_red(self) -> bool:
        """
        Checks if is a Reader
        """
        return False

    def __repr__(self):
        return f"<Admin: {self.username}"


class Reader(UserMixin, db.Model):
    """
    This holds the Reader table definition

    Attributes
    ----------
    username: str
        unique username of the reader
    password_hash: str
        hashed password

    Methods
    ----------
    is_administrator()
        checks if the user is an admin
    is_adred()
        checks if user is either an admin or reader
    is_red()
        checks if user is a reader
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    bills = db.relationship("Bill", backref="reader", lazy=True)

    def __init__(self, username: str, password_hash: str) -> None:
        self.id = int("2" + str(random.random())[2:10])
        self.username = username
        self.password_hash = password_hash

    @property
    def password(self):
        raise AttributeError("Password is Read Only!")

    def is_administrator(self) -> bool:
        """
        Checks if is an administrator
        """
        return True

    def is_adred(self) -> bool:
        """
        Checks if is either an administrator or reader
        """
        return True

    def is_red(self) -> bool:
        """
        Checks if is a Reader
        """
        return False

    def __repr__(self):
        return f"<Reader: {self.username}"


class Client(db.Model):
    """
    This holds the client table definition

    Attributes
    ----------
    username: str
        unique username of the client
    password_hash: str
        hashed password

    Methods
    ----------
    is_administrator()
        checks if the user is an admin
    is_adred()
        checks if user is either an admin or reader
    is_red()
        checks if user is a reader
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    bills = db.relationship("Bill", backref="client", lazy=True)

    def __init__(self, username: str, password_hash: str) -> None:
        self.id = int("3" + str(random.random())[2:10])
        self.username = username
        self.password_hash = password_hash

    @property
    def password(self):
        raise AttributeError("Password is Read Only!")

    def is_administrator(self) -> bool:
        """
        Checks if is an administrator
        """
        return True

    def is_adred(self) -> bool:
        """
        Checks if is either an administrator or reader
        """
        return True

    def is_red(self) -> bool:
        """
        Checks if is a Reader
        """
        return False

    def __repr__(self):
        return f"<Client: {self.username}>"


class Bill(db.Model):
    """
    A Class used to define the bill table

    Attributes
    ----------
    current_reading: int
        current meter reading
    read_on: date
        the date the reading was recorded
    client_id: int
        the id of the client owning the bill
    reader_id: int
        the id of the reader who recorded the bill
    """

    id = db.Column(db.Integer, primary_key=True)
    current_reading = db.Column(db.Integer, nullable=False)
    read_on = db.Column(db.DateTime, default=datetime.utcnow())
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    reader_id = db.Column(db.Integer, db.ForeignKey("reader.id"))

    def __repr__(self):
        return f"<Bill: {self.current_reading}>"


class AnonymousUser(AnonymousUserMixin):
    """
    Used to set an anonymouse user
    """

    def is_administrator(self):
        False
