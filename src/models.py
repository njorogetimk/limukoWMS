from datetime import datetime
import random
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, AnonymousUserMixin


db = SQLAlchemy()


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username):
        self.id = int("1" + str(random.random())[2:10])
        self.username = username

    @property
    def password(self):
        raise AttributeError("Password is Read Only!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, plain_text: str):
        return check_password_hash(self.password_hash, plain_text)

    def can(self):
        return True

    def is_admininistator(self):
        return True

    def __repr__(self):
        return f"<Admin: {self.username}"


class Reader(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    bills = db.relationship("Bill", backref="reader", lazy=True)

    def __init__(self, username):
        self.id = int("2" + str(random.random())[2:10])
        self.username = username

    @property
    def password(self):
        raise AttributeError("Password is Read Only!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, plain_text: str):
        return check_password_hash(self.password_hash, plain_text)

    def can(self):
        return False

    def is_admininistator(self):
        return False

    def __repr__(self):
        return f"<Reader: {self.username}"


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    bills = db.relationship("Bill", backref="client", lazy=True)

    def __init__(self, username):
        self.id = int("3" + str(random.random())[2:10])
        self.username = username

    @property
    def password(self):
        raise AttributeError("Password is Read Only!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, plain_text: str):
        return check_password_hash(self.password_hash, plain_text)

    def can(self):
        return False

    def is_admininistator(self):
        return False

    def __repr__(self):
        return f"<Client: {self.username}>"


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_reading = db.Column(db.Integer, nullable=False)
    read_on = db.Column(db.DateTime, default=datetime.utcnow())
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    reader_id = db.Column(db.Integer, db.ForeignKey("reader.id"))

    def __repr__(self):
        return f"<Bill: {self.current_reading}>"


class AnonymousUser(AnonymousUserMixin):
    def can(self):
        return False

    def is_administrator(self):
        False
