from unittest import TestCase

from app import app
from models import db, Pets

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class PetsModelTestCase(TestCase):
    """Tests for model for Pets."""

    def setUp(self):
        """Clean up any existing pets."""

        Pets.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()