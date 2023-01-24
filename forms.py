from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class AddPostForm(FlaskForm):
   """adding posts to blogly"""

   # name = StringField('Name')
   # creating dynamic selection field from users, above deprecated

   user = SelectField('User',
                     validators=[InputRequired()])
                     
   post = StringField('Post body',
                     validators=[InputRequired()])

class AddUserForm(FlaskForm):

   first_name = StringField('First name',
                           validators=[InputRequired()])
   last_name = StringField('Last name',
                           validators=[InputRequired()])
   img_url = StringField('Image URL')
