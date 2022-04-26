# Import Form and RecaptchaField (optional)

from flask_wtf import Form # RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextAreaField, PasswordField
# Import form validators
from wtforms.validators import InputRequired, Email, EqualTo

# Define the login form (WTForms)

class LoginForm(Form):
    email    = TextAreaField('Email Address', [Email(),
                InputRequired(message='Forgot your email address?')])
    password = PasswordField('Password', [
                InputRequired(message='Must provide a password. ;-)')])
