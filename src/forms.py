from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    role = SelectField(
        "Select Role",
        validators=[DataRequired()],
        choices=[
            ("admin", "Admin"),
            ("reader", "Reader"),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")


class AddUserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    role = SelectField(
        "Select Role",
        validators=[DataRequired()],
        choices=[
            ("admin", "Admin"),
            ("reader", "Reader"),
            ("client", "Client"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("verify_password", message="Passwords must match"),
        ],
    )
    verify_password = PasswordField("Confirm Password", validators=[DataRequired()])
