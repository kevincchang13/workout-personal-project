from flask import Blueprint, render_template, redirect, request, url_for
from project.models import Exercise, BodyPart
from project.exercises.forms import ExerciseForm
from project import db
from flask_login import login_required

exercises_blueprint = Blueprint('exercises', __name__, template_folder='templates')

@exercises_blueprint.route('/', methods = ['GET', 'POST'])
@login_required
def index():
	exercises = Exercise.query.order_by(Exercise.name).all()
	form = ExerciseForm(request.form)
	form.set_choices()
	if request.method == 'POST':
		if form.validate():
			new_exercise = Exercise(form.name.data, form.description.data)
			for bodypart in form.bodyparts.data:
				new_exercise.bodyparts.append(BodyPart.query.get_or_404(bodypart))
			db.session.add(new_exercise)
			db.session.commit()
			return redirect(url_for('exercises.index'))
		else:
			return render_template('exercises/new.html', form=form)
	return render_template('exercises/index.html', exercises=exercises)

@exercises_blueprint.route('/new')
@login_required
def new():
	form = ExerciseForm(request.form)
	form.set_choices()
	return render_template('exercises/new.html', form=form)

@exercises_blueprint.route('/<int:id>', methods = ["GET", "PATCH"])
@login_required
def show(id):
	exercise = Exercise.query.get_or_404(id)
	form = ExerciseForm(request.form)
	form.set_choices()
	if request.method == "PATCH":
		if form.validate():
			exercise.name = form.name.data
			exercise.description = form.description.data
			exercise.bodyparts = []
			for bodypart in form.bodyparts.data:
				exercise.bodyparts.append(BodyPart.query.get_or_404(bodypart))
			db.session.add(exercise)
			db.session.commit()
			return redirect(url_for('messages.index'))
		else:
			return render_template('exercises/edit.html', form=form, exercise=exercise)
	return render_template('exercises/show.html', exercise = exercise)

@exercises_blueprint.route('/<int:id>/edit')
@login_required
def edit(id):
	exercise = Exercise.query.get_or_404(id)
	bodyparts=[bodypart.id for bodypart in exercise.bodyparts]
	form = ExerciseForm(bodyparts=bodyparts)
	form.set_choices()
	form.description.data = exercise.description
	return render_template('exercises/edit.html', form=form, exercise=exercise)

@exercises_blueprint.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')


