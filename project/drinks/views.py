from flask import redirect, render_template, request, url_for, Blueprint, flash 
from project.drinks.models import Drink
from project.users.models import User
from project.users.views import ensure_correct_user
from project.drinks.forms import DrinkForm
from flask_login import current_user, login_required
from project import db
from sqlalchemy.exc import IntegrityError

drinks_blueprint = Blueprint(
  'drinks',
  __name__,
  template_folder='templates'
)

@drinks_blueprint.route('/', methods=["GET","POST"])
def index(id):
    if current_user.get_id() == str(id):
      form = DrinkForm()
      if form.validate():
        try:
          new_drink = Drink(
            user_id=id,
            name=form.name.data,
            username=form.username.data,
            ing1 = form.ing1.data,
            img = form.img.data,
            ing2 = form.ing2.data,
            ing3 = form.ing3.data,
            ing4 = form.ing4.data, 
            ing5 = form.ing5.data,
            ing6 = form.ing6.data,
            garnish = form.garnish.data,
            instructions = form.instructions.data
          )
          db.session.add(new_drink)
          db.session.commit()
        except IntegrityError as e:
            flash({'text': "Oops", 'status': 'danger'})
            return render_template('drinks/new.html', form=form)
        flash({'text': "Cool", 'status': 'success'})
        return redirect(url_for('root'))
    return render_template('drinks/new.html', id=id, form=form)

@drinks_blueprint.route('/new')
@login_required
@ensure_correct_user
def new(id):
  return render_template('drinks/new.html', form=DrinkForm(), user_id=id)

@drinks_blueprint.route('/<int:drink_id>', methods =["GET", "DELETE"])
def show(id, drink_id):
  found_drink = Drink.query.get(drink_id)
  if request.method == b"DELETE" and int(current_user.get_id()) == id:
    db.session.delete(found_drink)
    db.session.commit()
    return redirect(url_for('root', id=id))
  return render_template('drinks/show.html', drink=found_drink)