from flask import Flask, redirect, render_template, session, request, flash
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy
from models import connect_db, db, User, Post, get_posts, Comment
from forms import AddPostForm, AddUserForm

app = Flask(__name__)

# standardized sqlalchemy init setting and variable structure
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_db_ex1'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)
# app.debug = True

app.app_context().push()

connect_db(app)

@app.route('/')
def redirect_home():
   """sends to users page (home)"""
   return redirect('/users')

@app.route('/users', methods=["GET"])
def show_home():
   """displays homepage"""
   users = User.query.all()
   form = AddUserForm()
   return render_template('home.html', users=users, form=form)

@app.route('/users/add-user', methods=["POST"])
def create_user():
   """adds new user to database and webpage"""
   form = AddUserForm()
   first_name = form.first_name.data
   last_name = form.last_name.data
   img_url = form.img_url.data
   img_url = img_url if img_url else None

   new_user = User(first_name=first_name, last_name=last_name, img_url=img_url)
   db.session.add(new_user)
   db.session.commit()
   return redirect('/users')


@app.route('/users/<int:user_id>', methods=["POST", "GET"])
def show_user(user_id):
   """show details on specific user"""
   user = User.query.get_or_404(user_id)
   return render_template('user.html', user=user)

@app.route('/users/delete/<user_id>', methods=["POST", "GET"])
def delete_user(user_id):
   """delete user from detail page"""
   user = User.query.get_or_404(user_id)
   db.session.delete(user)
   db.session.commit();
   return redirect('/')

@app.route('/users/edit/<user_id>', methods=["POST", "GET"])
def show_edit_form(user_id):
   """shows edit form -- defaults = current values"""
   user = User.query.get_or_404(user_id)
   form = AddUserForm(obj=user)
   if form.is_submitted():
      first_name = form.first_name.data
      last_name = form.last_name.data
      img_url = form.img_url.data
      img_url = img_url if img_url else None

      user.first_name = first_name
      user.last_name = last_name
      user.img_url = img_url

      db.session.add(user)
      db.session.commit()
      return redirect(f'/users/{user.user_id}')


   else:
      return render_template('edit_user.html', user=user, form=form)

@app.route('/users/update/<user_id>', methods=["POST"])
def update_user(user_id):
   """updates user information with default values as current values"""
   

@app.route('/posts')
def show_posts():
   """shows posts page"""
   posts = Post.query.all()
   users = User.query.all()
   return render_template('posts.html', posts=posts, users=users)

# NEEDS FURTHER TESTING !!!!

@app.route('/posts/add', methods=["POST", "GET"])
def add_post():
   """shows post submission WTForms"""
   form = AddPostForm() 
   users = list(db.session.query(User.user_id, User.first_name))
   choices = []
   for user in users:
      choices.append(tuple(user))
   form.user.choices = choices
   if form.is_submitted():
      content = form.post.data
      user = form.user.data
      user_id = user

      post = Post(user_id=user_id, content=content)

      db.session.add(post)
      db.session.commit()
      return redirect('/posts')
   else:
      return render_template("add_post.html", form=form)


@app.route('/comments/<post_id>', methods=['GET'])
def show_comments(post_id):
   """displays comments associated with post"""
   post = Post.query.get(post_id)
   comments = Comment.query.filter_by(post_id=post_id)
   return render_template('comments.html', post=post, comments=comments)