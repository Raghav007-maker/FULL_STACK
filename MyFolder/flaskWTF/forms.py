from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[data_required(message="we need your name it not be empty")])
    email = StringField("Email", validators=[data_required(message="email message is required"), Email()])
    password = PasswordField("Password", validators=[data_required("password is required"), Length(min = 8, message="password must be atleast 6 character")])
    submit = SubmitField("Register")