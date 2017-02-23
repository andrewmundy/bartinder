from random import choice
from project import db, bcrypt
from flask_login import UserMixin


class User(db.Model, UserMixin):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	avatar = db.Column(db.Text)
	drinks = db.relationship('Drink', backref='user', lazy='dynamic')

	def __init__(self, username, password, avatar=None):
		if avatar is None:
			avatar = '/static/avatars/{}'.format(choice(['char.png','char2.png','char3.png','char4.png']))
		self.username = username
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
		self.avatar = avatar


