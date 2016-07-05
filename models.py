# -*- encoding: utf-8 -*-
# begin

from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from datetime import datetime
datetime.utcnow()
from app import db


db = SQLAlchemy(app)



class User(db.Model):
    #table name in database
    __table__name ="user"
    username = db.Column('username',  db.String, primary_key = True, unique=True)
    #email is unique
    email = db.Column('email', db.Unicode, unique= True)
    #password, max =255
    password = db.Column('password', db.String(255))
    confirm_password = db.Column('confirm_password', db.String)

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
    post = db.Column('post', db.String)
    creation_date = db.Column('creation_date', db.Date, default = datetime.utcnow)
    
    #user relation 
    username = relationship('User')
    username = db.Column(db.String, ForeignKey('user.username'))
    
    counsellor = relationship('Counsellor')
    counsellor_id = db.Column(db.String, ForeignKey('counsellor.counsellor_id'))
    
#    username = db.relationship('User', foreign keys = 'username')
#    counsellor_id = db.relationship('Counsellor', foreign keys = 'counsellor_id')

class Counsellor(db.Model):
    __tablename__  = "counsellor"
    #setting the counsellor_id to primary key 
    counsellor_id  = db.Column('counsellor_id',  db.String, primary_key = True, unique=True)
    name = db.Column('name',  db.String)
    email = db.Column('email', db.Unicode, unique= True)
    phone_number = db.Column('username',  db.Integer)
    avatar = db.Column('avatar', db.String)
    profession = db.Column('profession', db.String)
    about = db.Column('about', db.String)


class Comment(db.Model):
    __tablename__  = "comment"
    #setting the primary key to comment_id
    comment_id = db.Column('comment_id', db.String, primary_key = True, unique=True)
    message = db.Column('message', db.String)
    

	#creating relationships
    post = relationship('Posts')
    post_id = db.Column(db.String, ForeignKey('posts.post_id'))
    user = relationship('User')
    username = db.Column(db.String, ForeignKey('user.username'))
    counsellor = relationship('Counsellor')
    counsellor_id = db.Column(db.String, ForeignKey('counsellor.counsellor_id'))
        



class Likes(db.Model):
    __tablename__  = "likes"
# setting the primary key in message id 
    message = db.Column('message_id', db.String, primary_key = True, unique = True)

	#creating relationships
    post = relationship('Posts')
    post_id = db.Column(db.String, ForeignKey('posts.post_id'))
    user = relationship('User')
    username = db.Column(db.String, ForeignKey('user.username'))
    counsellor = relationship('Counsellor')
    counsellor_id = db.Column(db.String, ForeignKey('counsellor.counsellor_id'))
    comment =relationship('Comment', ForeignKey('comment.comment_id'))
    
    


    









