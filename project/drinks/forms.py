from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class DrinkForm(FlaskForm):
  name = StringField('name', validators=[DataRequired()])
  username = StringField('username')
  ing1 = StringField('ing1', validators=[DataRequired()])
  ing2 = StringField('ing2')
  ing3 = StringField('ing3')
  ing4 = StringField('ing4')
  ing5 = StringField('ing5')
  ing6 = StringField('ing6')
  garnish = StringField('garnish')
  instructions = StringField('instructions')
  img = StringField('img')