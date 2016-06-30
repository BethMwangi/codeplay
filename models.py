# -*- encoding: utf-8 -*-
# begin

from flask_sqlalchemy import SQLAlchemy
from wesupport import app

db = SQLAlchemy(app)

class User(db.Model):
    __table__name ="user"
    
    username = db.Column('username',  db.VarChar, primary_key = True)
    email = db.Column('email', db.Unicode)
    password = db.Column('password', db.VarChar)
    confirm_password = db.Column('confirm_password', db.VarChar)
    
    
class Posts(db.Model):
    __tablename__ ="posts"
    id = db.Column('post_id', db.Integer, primary_key = True)
    post = db.Column('post', db.VarChar)
    
    
