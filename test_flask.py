from unittest import TestCase

from app import app
from models import db, Pets

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class PetsViewsTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample pet."""

        Pets.query.delete()

        pet = Pets(name="TestPet", species="dog", hunger=10)
        db.session.add(pet)
        db.session.commit()

        self.id = pet.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()
