from flask import Flask, redirect, render_template, session, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import connect_db, db, User


app = Flask(__name__)

# standardized sqlalchemy init setting and variable structure **RUN BEFORE LINE 12**
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_db_ex1'

app.app_context().push()

db = SQLAlchemy(app)
# **app.config
db.app = app
db.init_app(app)

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.debug = True

app.app_context().push()

connect_db(app)

@app.route('/')
def show_home():
   """displays homepage"""
   users = User.query.all()
   return render_template('home.html', users=users)

@app.route('/', methods=["POST"])
def create_user():
   """adds new user to database and webpage"""
   first_name = request.form['fname']
   last_name = request.form['lname']
   img_url = request.form['img_url']
   img_url = img_url if img_url else None

   new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
   db.session.add(new_user)
   db.session.commit()
   return redirect(f'/users/{new_user.id}')


@app.route('/users/<int:user_id>')
def show_user(user_id):
   """show details on specific user"""
   user = User.query.get_or_404(user_id)
   return render_template('user.html', user=user)

@app.route('/users/delete/<user_id>', methods=["POST"])
def delete_user(user_id):
   """delete user from detail page"""
   user = User.query.get(user_id).delete()
   db.session.delete(user)
   db.session.commit();
   return redirect('/')

@app.route('/users/edit/<user_id>')
def show_edit_form(user_id):
   user = User.query.get(user_id)
   return render_template('edit_user.html', user=user)

