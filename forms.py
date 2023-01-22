from flask_wtf import FlaskForm
from wtforms.fields import Stringfield

class AddCommentForm(FlaskForm):
   """adding comments to blogly"""

   user = Stringfield('Username')
   content = Stringfield('Comment')