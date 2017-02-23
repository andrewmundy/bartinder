from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Length
# from wtforms.fields.html5 import EmailField  

class UserForm(FlaskForm):
  username = StringField('username', validators=[InputRequired("Please enter your username address.")])
  password = PasswordField('password', validators=[InputRequired("Reenter your password")])
  avatar = StringField('avatar')

class LoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[Length(min=6)])  