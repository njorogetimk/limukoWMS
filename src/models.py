from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Admin: {self.username}, Role: {self.role}>"


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    bills = db.relationship("Bill", backref="reader", lazy=True)

    def __repr__(self):
        return f"<Reader: {self.username}, Role: {self.role}>"


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    bills = db.relationship("Bill", backref="client", lazy=True)

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
