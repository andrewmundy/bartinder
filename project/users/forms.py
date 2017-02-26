from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired, DataRequired, Length
# from wtforms.fields.html5 import EmailField  

class UserForm(FlaskForm):
  username = StringField('username', validators=[InputRequired("Please enter a username.")])
  password = PasswordField('Password', [
    validators.DataRequired("Please enter a password."),
    validators.EqualTo('confirm', message="Passwords must match.")
  ])
  confirm = PasswordField('Repeat Password')

  avatar = StringField('avatar')

class LoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired("I think you forgot your username")])
  password = PasswordField('password', validators=[Length(min=6)]) 
  