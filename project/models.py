from project import db, bcrypt

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


	def __init__(self,name,description):
		self.name = name
		self.description = description

class BodyPart(db.Model):
	__tablename__ = 'bodyparts'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, unique = True)

	def __init__(self,name):
		self.name=name


