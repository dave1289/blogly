from flask_wtf import FlaskForm
from wtforms import StringField

class AddCommentForm(FlaskForm):
   """adding comments to blogly"""

   user = StringField('Username')
   content = StringField('Comment')