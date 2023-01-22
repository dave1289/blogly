from flask_wtf import FlaskForm
from wtforms import StringField

class AddCommentForm(FlaskForm):
   """adding comments to blogly"""

   user = StringField('Username')
   Post = StringField('Post body')

class AddUserForm(FlaskForm):

   first_name = StringField('First name')
   last_name = StringField('Last name')
   img_url = StringField('Image URL')