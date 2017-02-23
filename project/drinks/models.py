from project import db 
from random import choice


class Drink(db.Model):
  
  __tablename__ = 'drinks'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(140))
  username = db.Column(db.String)
  img = db.Column(db.String)
  ing1 = db.Column(db.String)
  ing2 = db.Column(db.String)
  ing3 = db.Column(db.String)
  ing4 = db.Column(db.String)
  ing5 = db.Column(db.String)
  ing6 = db.Column(db.String)
  garnish = db.Column(db.String)
  instructions = db.Column(db.String)
  likes = db.Column(db.Integer)
  dislikes = db.Column(db.Integer)
  favorite = db.Column(db.Integer)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

  def __init__(self, username, ing1=None, name=None, ing3=None, ing4=None, ing5=None, ing6=None, garnish=None, instructions=None, likes=None, dislikes=None, favorite=None, user_id=None, img=None, ing2=None):
    if img is "":
      img = choice(['http://s3.amazonaws.com/auteurs_production/images/film/cocktail/w1280/cocktail.jpg',
      'https://s-media-cache-ak0.pinimg.com/originals/d6/90/37/d69037f83ebde80a94cd2e23d8a8a617.jpg',
      'http://i.dailymail.co.uk/i/pix/2014/11/09/1415515863112_wps_42_Shark_Bite.jpg'
    ])

    self.user_id = user_id
    self.name = name
    self.username = username
    self.ing1 = ing1
    self.ing2 = ing2
    self.ing3 = ing3
    self.ing4 = ing4
    self.ing5 = ing5
    self.ing6 = ing6
    self.garnish = garnish
    self.instructions = instructions
    self.likes = likes
    self.dislikes = dislikes
    self.favorite = favorite
    self.img = img
