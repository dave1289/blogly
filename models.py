from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
   db.app = app
   db.init_app(app)

class User(db.Model):
   __tablename__ = 'users'

   def __repr__(self):
      p = self
      return f'USER id={p.id} first_name={p.first_name} last_name={p.last_name} image_url={p.img_url}'

   id = db.Column(db.Integer,
                  primary_key=True,
                  autoincrement=True)

   first_name = db.Column(db.Text,
                           nullable=False)

   last_name = db.Column(db.Text,
                           nullable=False)

   img_url = db.Column(db.Text, default='None')

   def get_full_name(self):
      full_name = f'{self.first_name} {self.last_name}'
      return full_name