from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/workouts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')

from project.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='root'
login_manager.login_message='Please log in.'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


from project.exercises.views import exercises_blueprint
app.register_blueprint(exercises_blueprint, url_prefix='/exercises')

from project.bodyparts.views import bodyparts_blueprint
app.register_blueprint(bodyparts_blueprint, url_prefix='/bodyparts')

from project.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/users')

from project.users.forms import LoginForm, SignUpForm

@app.route('/')
def root():
	login_form = LoginForm(request.form)
	signup_form = SignUpForm(request.form)
	return render_template('home.html', login_form=login_form, signup_form=signup_form)

@app.route('/about')
def about():
	form = LoginForm(request.form)
	return render_template('about.html', form=form)
