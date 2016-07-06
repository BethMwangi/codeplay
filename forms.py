from flask_wtf import Form

<<<<<<< HEAD
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, Email,
=======
from wtforms import StringField, PasswordField, TextAreaField 
from wtforms.validators import (DataRequired, Regexp, Email, 
>>>>>>> b451b4878ac4361f5855ce71873f7c79a3f4b8f0
                                Length, EqualTo, ValidationError)
from models import User, UserMixin


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


def email_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')


class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[ a-zA-Z0-9_]+$',
                message=("username should be one word, letters, "
<<<<<<< HEAD
                         " numbers, and underscores only")
=======
                         " numbers, andd underscores only")
>>>>>>> b451b4878ac4361f5855ce71873f7c79a3f4b8f0
            ),
            name_exists])

    email = StringField(

        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwordmust match')]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class PostForm(Form):
<<<<<<< HEAD
  content = TextAreaField("what's app", validators=[DataRequired()])

=======
	content = TextAreaField("what's app", validators=[DataRequired()])
>>>>>>> b451b4878ac4361f5855ce71873f7c79a3f4b8f0

class CounsellorForm(Form):
    name = StringField(
        'Full name',
        validators=[
            DataRequired(),
            Regexp(
                r'^[ a-zA-Z0-9_]+$',
                message=("Name should be one word, letters, "
                         " numbers, and underscores only")
            ),
            name_exists])
    email = StringField(

        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists])
    profession = StringField(
        'Profession',
        validators=[
            DataRequired()])
    phone= StringField(
        'Phone number',
        validators=[
            DataRequired()])
    counsellor_id= StringField(
        'Counsellor id',
        validators=[
            DataRequired()])
    location =StringField(
        'Location',
        validators=[
            DataRequired()])
<<<<<<< HEAD

=======
>>>>>>> b451b4878ac4361f5855ce71873f7c79a3f4b8f0
