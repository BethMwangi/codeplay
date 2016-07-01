from wtforms import Form, TextField, SubmitField, validators, ValidationError, PasswordField

class SignupForm(Form):
	username = TextField("Username",  [validators.Required()])
	email = TextField("Email",  [validators.Required(), validators.Email()])
	password = PasswordField('Password', [validators.Required()])
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
