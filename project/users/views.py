from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project.users.forms import UserForm
from project import db,bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('id') != current_user.id:
            flash({'text': "Not Authorized", 'status': 'danger'})
            return redirect(url_for('root'))
        return fn(*args, **kwargs)
    return wrapper

@users_blueprint.route('/')
@login_required
def home():
    return render_template('home.html')

@users_blueprint.route('/signup', methods =["GET", "POST"])
def signup():
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            try:
                new_user = User(
                  username=form.username.data,
                  password=form.password.data
                )
                if form.avatar.data:
                    new_user.avatar = form.avatar.data
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
            except IntegrityError as e:
                flash({'text': "Username already taken", 'status': 'danger'})
                return render_template('users/signup.html', form=form)
            flash({'text': "Oh hey {}, welcome to Bartinder!".format(new_user.username), 'status': 'success'})
            return redirect(url_for('root'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            found_user = User.query.filter_by(username = form.username.data).first()
            if found_user:
                authenticated_user = bcrypt.check_password_hash(found_user.password, form.password.data)
                if authenticated_user:
                    login_user(found_user)
                    flash({'text': "Hello, {}!".format(found_user.username), 'status': 'success'})
                    return redirect(url_for('root'))
        flash({'text': "Invalid credentials.", 'status': 'danger'})
        return render_template('users/login.html', form=form)
    return render_template('users/login.html', form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash({ 'text': "You have successfully logged out.", 'status': 'success' })
    return redirect(url_for('users.login'))

@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
  return render_template('users/edit.html', form=UserForm(), user=User.query.get(id))

@users_blueprint.route('/<int:id>', methods =["GET", "PATCH", "DELETE"])
@ensure_correct_user
@login_required
def show(id):
    found_user = User.query.get(id)
    if request.method == b"PATCH":
        form = UserForm(request.form)
        if form.validate():
            found_user.username = request.form['username']
            found_user.password = bcrypt.generate_password_hash(request.form['password']).decode('UTF-8')
            found_user.avatar = request.form['avatar']
            db.session.add(found_user)
            db.session.commit()
            return redirect(url_for('users.home'))
        return render_template('users/edit.html', form=form, user=found_user)
    if request.method == b"DELETE":
        db.session.delete(found_user)
        db.session.commit()
        logout_user() 
        return redirect(url_for('users.home'))
    return render_template('users/show.html', user=found_user)
