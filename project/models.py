from project import db, bcrypt
from flask_login import UserMixin

BodyPartExercise = db.Table('bodypart_exercises',
							db.Column('id', db.Integer, primary_key=True),
							db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id', ondelete='cascade')),
							db.Column('bodypart_id', db.Integer, db.ForeignKey('bodyparts.id', ondelete='cascade'))
							)

class Exercise(db.Model):
	__tablename__ = 'exercises'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, unique = True)
	description = db.Column(db.Text)
	bodyparts = db.relationship('BodyPart', secondary=BodyPartExercise, backref=db.backref('exercises'))


	def __init__(self,name,description):
		self.name = name
		self.description = description

class BodyPart(db.Model):
	__tablename__ = 'bodyparts'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, unique = True)

	def __init__(self,name):
		self.name=name


class User(db.Model, UserMixin):
	__tablename__='users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	email = db.Column(db.Text)

	def __init__(self,username,password,email):
		self.username = username
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
		self.email = email

	@classmethod
	def authenticate(cls, username, password):
		user = cls.query.filter_by(username=username).first()
		if user:
			authenticated_user=bcrypt.check_password_hash(user.password, password)
			if authenticated_user:
				return user
		return False
