from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class AddPostForm(FlaskForm):
   """adding posts to blogly"""

   # name = StringField('Name')
   # creating dynamic selection field from users, above deprecated

   user = SelectField('User')
   post = StringField('Post body')

class AddUserForm(FlaskForm):

   first_name = StringField('First name')
   last_name = StringField('Last name')
   img_url = StringField('Image URL')