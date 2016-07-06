import datetime

from flask_bcrypt import generate_password_hash

from flask_login import UserMixin
import peewee
from sqlalchemy import ForeignKey
<<<<<<< HEAD
=======
from peewee import *
>>>>>>> b451b4878ac4361f5855ce71873f7c79a3f4b8f0





DATABASE = peewee.PostgresqlDatabase('wesupport', user="postgres")


class User(UserMixin, peewee.Model):
    username = peewee.CharField(unique=True)
    email = peewee.CharField(unique=True)
    password = peewee.CharField(max_length=100)
    is_admin = peewee.BooleanField(default=False)

    class Meta:
        database = DATABASE

    def get_posts(self):
        return Post.select().where(Post.user == self)

    def get_stream(self):
        return Post.select().where(
            (Post.user == self)
        )


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            with DATABASE.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password=generate_password_hash(password),
                    is_admin=admin)

        except peewee.IntegrityError:
            raise ValueError('User already exists')


<<<<<<< HEAD
class Post(peewee.Model):
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    user = peewee.ForeignKeyField(
        rel_model=User,
        related_name='posts'

    )
    content = peewee.TextField()

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


# class Relationship(peewee.Model):
#     from_user = ForeignKey(User, related_name="relationships")
#     to_user = ForeignKey(User, related_name="related_to")
#
#     class Meta:
#         database = DATABASE
#         indexes = (
#             (('from_user', 'to_user'), True)
#         )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post], safe=True)
    DATABASE.close()
=======


class Counsellor(peewee.Model):
    name = peewee.CharField(unique=True)
    counsellor_id = peewee.CharField(max_length=100)
    # tel_no = peewee.IntegerField(max_length=100)
    email = peewee.CharField(unique=True)
    password = peewee.CharField(max_length=100)
    profession = peewee.CharField()
    is_admin = peewee.BooleanField(default=False)
    about = peewee.CharField(max_length=200)

    class Meta:
        database = DATABASE



class Post(peewee.Model):
    user = ForeignKeyField(User, related_name='posts')
    post = TextField()
    post_id =  peewee.CharField(max_length=100)
    timestamp = peewee.DateTimeField(default = datetime.datetime.now)

    class Meta:
        order_by = ('-timestamp',)
        database = DATABASE
       
class Comment(peewee.Model):
    user = ForeignKeyField(User, related_name='comments')
    Comment = TextField()
    comment_id =  peewee.CharField(max_length=100)
    timestamp = peewee.DateTimeField(default = datetime.datetime.now)

    class Meta:    
        order_by = ('-timestamp',)
        database = DATABASE

class Like(peewee.Model):
    comment = ForeignKeyField(User, related_name='likes')
    user = ForeignKeyField(User, related_name='like')
    like_id =  peewee.CharField
    timestamp = peewee.DateTimeField(default = datetime.datetime.now)

    class Meta:    
        order_by = ('-timestamp',)
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post, Counsellor, Comment, Like], safe = True)
    DATABASE.close()


>>>>>>> b451b4878ac4361f5855ce71873f7c79a3f4b8f0
