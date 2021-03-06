from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

class SignUpForm(FlaskForm):
	username=StringField('username', validators=[DataRequired()])
	password=PasswordField('password', validators=[DataRequired()])
	email=StringField('email', validators=[DataRequired()])

class EditUserForm(FlaskForm):
	username=StringField('username', validators=[DataRequired()])
	email=StringField('email', validators=[DataRequired()])
