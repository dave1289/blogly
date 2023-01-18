from models import User, db, Post
from app import app

# create tables
db.drop_all()
db.create_all()

# empty tables
Post.query.delete()
User.query.delete()

# create users
whiskey = User(first_name='Whiskey', last_name='Daniels', img_url='sadbrad.com')
bowser = User(first_name='Bowser', last_name = 'Mariosenti')
spike = User(first_name='Spike', last_name='Spiegel', img_url='cowboybebop.com')
dave = User(first_name='Dave', last_name='McElhaney', img_url='facebook.com/dave')
james = User(first_name='James', last_name='McElhaney')

# add users to psql session

db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)
db.session.add(dave)
db.session.add(james)

# 
db.session.commit()

# create posts
post_1 = Post(user_id=1, content='Well that is just great... I lost my Flenck')
post_2 = Post(user_id=3, content='This one might work...')
post_3 = Post(user_id=3, content='This is a real post you posty posthole')
post_4 = Post(user_id=3, content='I am the best poster on this site')
post_5 = Post(user_id=5, content='James checking in')
post_6 = Post(user_id=4, content='Bruj... I see you')
post_7 = Post(user_id=1, content='Guys this is weird')

# add posts to session
db.session.add(post_1)
db.session.add(post_2)
db.session.add(post_3)
db.session.add(post_4)
db.session.add(post_5)
db.session.add(post_6)
db.session.add(post_7)

# commit post changes to session
db.session.commit()
