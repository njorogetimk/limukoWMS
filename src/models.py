from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    Roles:
        1. Admin
        2. Reader
        3. Client
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User: {self.username}, Role: {self.role}>"


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_reading = db.Column(db.Integer, nullable=False)
    read_on = db.Column(db.DateTime(), nullable=False)
    reader = db.Column(db.String(100), nullable=False)
    client = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Bill: {self.current_reading}>"
