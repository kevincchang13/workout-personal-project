from flask import Flask, render_template, g
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/workouts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
csrf = CSRFProtect(app)

from project.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='root'
login_manager.login_message='Please log in.'
login_manager.login_message_category='alert-warning'

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
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.before_request
def login_signup_form():
	if not current_user.is_authenticated:
		g.login_form=LoginForm()
		g.signup_form=SignUpForm()


