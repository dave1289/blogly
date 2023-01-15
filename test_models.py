from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
   """Tests for model for User."""

   def setUp(self):
      """Clean up any existing User."""

      User.query.delete()

   def tearDown(self):
      """Clean up any fouled transaction."""

      db.session.rollback()
   
   def test_get_by_id(self):
      """test getting by id"""
      user = User(first_name="Test", last_name="Human", img_url="")
      db.session.add(user)
      db.session.commit()

      found_user = User.get_by_id(user.id)
      self.assertEquals(found_user, [user])

   def test_get_full_name(self):
      """tests that get_full_name() matches fstring concat first+last"""
      user = User(first_name="Test", last_name="Human", img_url="")
      full_name = user.get_full_name()
      manual_fname = f'{user.first_name} {user.last_name}'

      self.assertEquals(full_name, manual_fname)