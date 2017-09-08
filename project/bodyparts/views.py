from flask import Blueprint, render_template, redirect, request, url_for
from project.models import BodyPart, Exercise
from project.bodyparts.forms import BodyPartForm
from project import db
from flask_login import login_required

bodyparts_blueprint = Blueprint('bodyparts', __name__, template_folder='templates')

@bodyparts_blueprint.route('/', methods = ["GET", "POST"])
@login_required
def index():
	form = BodyPartForm(request.form)
	form.set_choices()
	if request.method =='POST':
		if form.validate():
			bodypart = BodyPart(form.name.data)
			for exercise in form.exercises.data:
				bodypart.exercises.append(Exercise.query.get_or_404(exercise))
			db.session.add(bodypart)
			db.session.commit()
			return redirect(url_for('bodyparts.show', id=bodypart.id))
		else:
			return render_template('bodyparts/new.html', form=form)
	return render_template('bodyparts/new.html', form=form)


@bodyparts_blueprint.route('/new')
@login_required
def new():
	form = BodyPartForm(request.form)
	form.set_choices()
	return render_template('bodyparts/new.html', form=form)

@bodyparts_blueprint.route('/<int:id>', methods=['GET', 'PATCH'])
@login_required
def show(id):
	bodypart=BodyPart.query.get_or_404(id)
	form=BodyPartForm(request.form)
	form.set_choices()
	if request.method == b'PATCH':
		if form.validate():
			bodypart.name = form.name.data
			bodypart.exercises =[]
			for exercise in form.exercises.data:
				bodypart.exercises.append(Exercise.query.get_or_404(exercise))
			db.session.add(bodypart)
			db.session.commit()
			return redirect(url_for('bodyparts.show', id=id))
		else:
			return render_template('bodyparts/edit.html', form=form, bodypart=bodypart)
	return render_template('bodyparts/show.html', bodypart=bodypart)

@bodyparts_blueprint.route('/<int:id>/edit')
@login_required
def edit(id):
	bodypart=BodyPart.query.get_or_404(id)
	exercises=[exercise.id for exercise in bodypart.exercises]
	form = BodyPartForm(exercises=exercises)
	form.set_choices()
	return render_template('bodyparts/edit.html', form=form, bodypart=bodypart)


@bodyparts_blueprint.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')


