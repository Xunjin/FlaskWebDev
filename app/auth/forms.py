from flask_wtf import FlaskForm
from wtforms import Stringfield, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = Stringfield('Email', validators=[DataRequired(), Length(1, 64),
                        Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')
