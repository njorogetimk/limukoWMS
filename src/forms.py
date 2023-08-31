from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    """
    Defines the login form

    Attributes
    ----------
    username : str
        username of the user
    role : str
        the role of the user
    password : str
        pasword of the user
    """

    username = StringField("Username", validators=[DataRequired()])
    role = SelectField(
        "Select Role",
        validators=[DataRequired()],
        choices=[
            ("admin", "Admin"),
            ("reader", "Reader"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Remember me")


class AddUserForm(FlaskForm):
    """
    Defines the add use form

    Attributes
    ----------
    username : str
        username of the user
    role : str
        the role of the user
    password : str
        pasword of the user
    verify_password : str
        verify the password input
    """

    username = StringField("Username", validators=[DataRequired()])
    role = SelectField(
        "Select Role",
        validators=[
            DataRequired(),
        ],
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
            Length(8),
        ],
    )
    verify_password = PasswordField("Confirm Password", validators=[DataRequired()])
