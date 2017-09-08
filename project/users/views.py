from flask import Blueprint, render_template, redirect, request, url_for, flash
from project.models import User
from project import db
from sqlalchemy.exc import IntegrityError
from project.users.forms import LoginForm, SignUpForm, EditUserForm
from flask_login import logout_user, login_user, current_user, login_required
from functools import wraps

users_blueprint = Blueprint('users', __name__, template_folder='templates')

def ensure_correct_user(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs.get('id') != current_user.id:
			flash('Not Authorized', 'alert-warning')
			return redirect(url_for('exercises.index'))
		return fn(*args, **kwargs)
	return wrapper

@users_blueprint.route('/login', methods=["GET","POST"])
def login():
	login_form = LoginForm(request.form)
	if request.method == 'POST':
		if login_form.validate():
			user=User.authenticate(request.form.get('username'), request.form.get('password'))
			if user:
				login_user(user)
				flash('You successfully logged in!', 'alert-success')
				return redirect(url_for('exercises.index'))
		flash('Invalid credentials.', 'alert-warning')
		return redirect(url_for('root'))
	return redirect(url_for('root'))


@users_blueprint.route('/signup', methods=["GET", "POST"])
def signup():
	signup_form = SignUpForm(request.form)
	if request.method == 'POST':
		if signup_form.validate():
			try:
				user=User(signup_form.username.data, signup_form.password.data, signup_form.email.data)
				db.session.add(user)
				db.session.commit()
			except IntegrityError as e:
				flash('Invalid submission. Please try again.', 'alert-warning')
				return redirect(url_for('root'))
			login_user(user)
			flash('Successfully signed up!', 'alert-success')
			flash('You have been logged in!', 'alert-success')
			return redirect(url_for('exercises.index'))
		flash('Invalid submission. Please try again.', 'alert-warning')
		return redirect(url_for('root'))
	return redirect(url_for('root'))



@users_blueprint.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been signed out.', 'alert-success')
	return redirect(url_for('root'))



@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
	user = User.query.get_or_404(id)
	form = EditUserForm(user=user)
	return render_template("users/edit.html", form=form, user=user)


@users_blueprint.route('/<int:id>', methods =['GET', 'PATCH'])
@login_required
def show(id):
	user=User.query.get_or_404(id)
	form = EditUserForm(request.form)
	if request.method == b'PATCH':
		if form.validate():
			user.username = form.username.data
			user.email = form.email.data
			db.session.add(user)
			db.session.commit()
			flash('Successfully Edited Profile', 'alert-success')
			return redirect(url_for('users.edit', id=user.id))
		else:
			flash('Invalid submission.', 'alert-warning')
			return render_template('users/edit.html', form=form, user=user)
	return render_template('users/show.html')


# @users_blueprint.route('/', methods = ["GET", "POST"])
# def index():
# 	pass

# @users_blueprint.route('/new')
# def new():
# 	pass

# @users_blueprint.route('/<int:id>', methods=['GET', 'PATCH'])
# def show(id):
# 	pass




@users_blueprint.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')


