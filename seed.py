"""Seed file to make sample data for Pets db"""

from models import User, db
from app import app

# create tables
db.drop_all()
db.create_all()

# empty tables
User.query.delete()

# create pets
whiskey = User(first_name='Whiskey', last_name='Daniels', image_url='sadbrad.com')
bowser = User(first_name='Bowser', last_name = 'Mariosenti')
spike = User(first_name='Spike', last_name='Spiegel', image_url='cowboybebop.com')

# add pets to psql session
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# commit changes to session
db.session.commit()
