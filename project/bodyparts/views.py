from flask import Blueprint
from project.models import BodyPart
from project import db

bodyparts_blueprint = Blueprint('bodyparts', __name__, template_folder='tempaltes')

