from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    role = SelectField(
        "Role",
        validators=[DataRequired()],
        choices=[
            ("choose disabled", "Select your role"),
            ("admin", "Admin"),
            ("reader", "Reader"),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
