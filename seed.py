from models import User, db, Post, Comment, User_Post
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
post_3 = Post(user_id=2, content='This is a real post you posty posthole')
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

# populate user_posts
entry_1 = User_Post(user_id= 1, post_id=1)
entry_2 = User_Post(user_id= 3, post_id=2)
entry_3 = User_Post(user_id= 2, post_id=3)
entry_4 = User_Post(user_id= 3, post_id=4)
entry_5 = User_Post(user_id= 5, post_id=5)
entry_6 = User_Post(user_id= 4, post_id=6)
entry_7 = User_Post(user_id= 1, post_id=7)

# add entries to user_post session
db.session.add(entry_1)
db.session.add(entry_2)
db.session.add(entry_3)
db.session.add(entry_4)
db.session.add(entry_5)
db.session.add(entry_6)
db.session.add(entry_7)

# commit user_posts entries
db.session.commit()

# populate comments
comment_1 = Comment(comment_id=1, user_id=2, post_id=2, comment='Woah im commenting!')
comment_2 = Comment(comment_id=2, user_id=3, post_id=4, comment='Dude my yams got SLAMMED')
comment_3 = Comment(comment_id=3, user_id=3, post_id=1, comment='This is how we do it.')
comment_4 = Comment(comment_id=4, user_id=3, post_id=3, comment='Thats a sick Flenck')
comment_5 = Comment(comment_id=5, user_id=1, post_id=4, comment='Where my cats at?!')
comment_6 = Comment(comment_id=6, user_id=4, post_id=4, comment='Found a SICK planche down at the bayou!')
comment_7 = Comment(comment_id=7, user_id=2, post_id=1, comment='CALIFORNIA ISNT REAL')
comment_8 = Comment(comment_id=8, user_id=1, post_id=5, comment='Shiny rocks > matte rocks')
comment_9 = Comment(comment_id=9, user_id=5, post_id=3, comment='Where am i?')
comment_10 = Comment(comment_id=10, user_id=4, post_id=1, comment='ITS DARK HERE')

# add comments to session
db.session.add(comment_1)
db.session.add(comment_2)
db.session.add(comment_3)
db.session.add(comment_4)
db.session.add(comment_5)
db.session.add(comment_6)
db.session.add(comment_7)
db.session.add(comment_8)
db.session.add(comment_9)
db.session.add(comment_10)

# commit comments to db
db.session.commit()
