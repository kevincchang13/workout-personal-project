from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Exercise

class MultiCheckField(SelectMultipleField):
	widget=widgets.ListWidget(prefix_label=False)
	option_widget=widgets.CheckboxInput()

class BodyPartForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	exercises = MultiCheckField('Exercises', coerce=int)


	def set_choices(self):
		self.exercises.choices=[(e.id, e.name) for e in Exercise.query.all()]
