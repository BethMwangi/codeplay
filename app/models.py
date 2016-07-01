# -*- encoding: utf-8 -*-
# begin

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
datetime.utcnow()
#from app import db

db = SQLAlchemy(app)

class User(db.Model):
    __table__name ="user"
    username = db.Column('username',  db.VarChar, primary_key = True, unique=True)
    email = db.Column('email', db.Unicode, unique= True)
    password = db.Column('password', db.VarChar)
    confirm_password = db.Column('confirm_password', db.VarChar)

	def __init__(self, username, email, password):
    self.username = firstname.title()
    self.email = email.lower()
    self.set_password(password)

    def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
    return check_password_hash(self.pwdhash, password)


class Posts(db.Model):
    __tablename__ ="posts"
    post_id = db.Column('post_id', db.Integer, primary_key = True)
    post = db.Column('post', db.VarChar)

    username = db.relationship('User', foreign_keys = username)
    counsellor_id = db.relationship('Counsellor', foreign keys = counsellor_id)

class Counsellor(db.Model):
    __tablename__  = "counsellor"
    counsellor_id  = db.Column('counsellor_id',  db.VarChar, primary_key = True, unique=True)
    name = db.Column('username',  db.VarChar)
    email = db.Column('email', db.Unicode, unique= True)
    phone_number = db.Column('username',  db.Integer)
    avatar = db.Column('avatar', db.blob)
    profession = db.Column('profession', db.VarChar)
    about = db.Column('about', db.VarChar)


class Comment(db.Model)
    __tablename__  = "comment"
    comment_id = db.Column('comment_id', db.VarChar, primary_key = True, unique=True)
    message = db.Column('message', db.VarChar)

	#creating relationships
    post_id = db.relationship('Posts', foreignkeys = post_id)
    username = db.relationship('User', foreignkeys = username)
    counsellor = db.relationship('Counsellor', foreignkeys = counsellor_id)

class Likes
     __tablename__  = "likes"
    message = db.Column('message', db.VarChar )

	#creating relationships
    post_id = db.relationship('Posts', foreignkeys = post_id)
    username = db.relationship('User', foreignkeys = username)
    counsellor = db.relationship('Counsellor', foreignkeys = counsellor_id)
    comment = db.relationship('Comment', foreignkeys = comment_id)









