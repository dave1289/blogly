from unittest import TestCase

from app import app
from models import db, User

# ***********************************************************************************
# TEST DEPEND ON INCLUDED SEED FILE
# *********************************************************************************

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db_test'
app.config['SQLALCHEMY_ECHO'] = False
# BELOW IS ONLY FOR TESTING
app.config['WTF_CSRF_ENABLED'] = False
# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Tests for views for User."""

    def setUp(self):
        """Add sample user."""

        User.query.delete()

        user = User(first_name="Test", last_name="Human", img_url="")
        db.session.add(user)
        db.session.commit()

        self.id = user.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_home(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('BlogLy', html)
    
    def test_post_table(self):
        with app.test_client() as client:
            resp = client.get('/posts')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Flenck', html)

    def test_add_user(self):
        with app.test_client() as client:
            resp = client.get('')
