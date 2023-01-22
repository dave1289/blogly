from flask_wtf import FlaskForm
from wtforms import StringField

class AddPostForm(FlaskForm):
   """adding posts to blogly"""

   name = StringField('Name')
   post = StringField('Post body')

class AddUserForm(FlaskForm):

   first_name = StringField('First name')
   last_name = StringField('Last name')
   img_url = StringField('Image URL')