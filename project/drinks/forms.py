from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, Form
from wtforms.validators import DataRequired

choices = [('.25oz', '.25oz'),('.5oz', '.5oz'), ('1oz', '1oz'), ('2oz', '2oz'), ('Dash', 'Dash'), ('','-')]

class DrinkForm(FlaskForm):
  name = StringField('name', validators=[DataRequired("Hi")])
  username = StringField('username')
  ing1 = StringField('ing1', validators=[DataRequired("Hey")])
  measurments1 = SelectField(u'Measurements', choices = choices)
  ing2 = StringField('ing2')
  measurments2 = SelectField(u'Measurements', choices = choices)
  ing3 = StringField('ing3')
  measurments3 = SelectField(u'Measurements', choices = choices)
  ing4 = StringField('ing4')
  measurments4 = SelectField(u'Measurements', choices = choices)
  ing5 = StringField('ing5')
  measurments5 = SelectField(u'Measurements', choices = choices)
  ing6 = StringField('ing6')
  measurments6 = SelectField(u'Measurements', choices = choices)
  garnish = StringField('garnish')
  instructions = StringField('instructions')
  img = StringField('img')

  measurments = [measurments1, measurments2, measurments3, measurments4, measurments5, measurments6]

# "3oz tequila"