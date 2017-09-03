from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://localhost/workouts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')

from project.exercises.views import exercises_blueprint
app.register_blueprint(exercises_blueprint, url_prefix='/exercises')

from project.bodyparts.views import bodyparts_blueprint
app.register_blueprint(bodyparts_blueprint, url_prefix='/bodyparts')

@app.route('/')
def root():
	return render_template('home.html')
