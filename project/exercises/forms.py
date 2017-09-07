from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import BodyPart
from wtforms.widgets import TextArea

class MultiCheckField(SelectMultipleField):
	widget=widgets.ListWidget(prefix_label=False)
	option_widget=widgets.CheckboxInput()

class ExerciseForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	description = StringField('description', widget=TextArea())
	bodyparts = MultiCheckField('BodyParts', coerce=int)

	def set_choices(self):
		self.bodyparts.choices=[(bp.id, bp.name) for bp in BodyPart.query.all()]
