from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
   db.app = app
   db.init_app(app)

class User(db.Model):
   """blogly users"""
   __tablename__ = 'users'

   @classmethod
   def get_by_id(cls, id):
      return cls.query.filter_by(id=id).one()

   def __repr__(self):
      p = self
      return f'<USER id={p.user_id} first_name={p.first_name} last_name={p.last_name} image_url={p.img_url}>'

   user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   first_name = db.Column(db.Text, nullable=False)
   last_name = db.Column(db.Text, nullable=False)
   img_url = db.Column(db.Text, default='None')

   def get_full_name(self):
      full_name = f'{self.first_name} {self.last_name}'
      return full_name


class Post(db.Model):
   """blogly posts by post_id user_id -> users"""
   __tablename__ = 'posts'

   def __repr__(self):
      p = self
      return f'<POST id={p.post_id} user={p.user_id} content={p.content}>'

   post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
   content = db.Column(db.String(120), nullable=False)

   # adds ability to pull POST.**post_user**(from below) to pull properties from user associated with post
   # ie ... test_post.post_user.first_name gives us user.first_name attached to post
   poster = db.relationship('User', backref='posts')

def get_posts():
   all_users = User.query.all()
   for user in all_users:
      if user.posts is not None:
         for post in user.posts:
            print(user.get_full_name(), post)
      elif user.posts is None:
         print(user.get_full_name())