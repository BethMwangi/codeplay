from wtforms import TextAreaField, TextField, SubmitField, validators, ValidationError, PasswordField
from flask.ext.wtf import Form
from wtforms.validators import DataRequired, Length, Email, EqualTo
class SignupForm(Form):
	username = TextField("Username",  [validators.DataRequired()])
	email = TextField("Email",  [validators.DataRequired(), validators.Email()])
	password = PasswordField('Password', [validators.DataRequired()])
	submit = SubmitField("Register")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False
		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user:
		  	self.email.errors.append("That email is already taken")
		  	return False
		else:
		  	return True

#================================ posts form==================

class PostForm(Form):
	post = TextAreaField("Have anything to share? Post it here", validators=[DataRequired()])
	submit = SubmitField()

def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

def validate(self):
	if not Form.validate(self):
		return 'all fields must be filled'
	else:
		return True