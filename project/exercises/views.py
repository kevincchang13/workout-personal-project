from flask import Blueprint
from project.models import Exercise
from project import db

exercises_blueprint = Blueprint('exercises', __name__, template_folder='tempaltes')

