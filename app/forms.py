from wtforms import  TextField, SubmitField, validators, ValidationError, PasswordField, BooleanField
from flask.ext.wtf import Form
from wtforms.validators import Required
#from models import User, Posts


#the login form

class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
    remember = BooleanField('Remember me')
    
    
    def validate(self):
        """ Verify login credentials."""
        if not Form.validate(self):
            return False
        self.user = User.query.filter_by_name(self.username.data)
        
        #valid username?
        if not self.user:
            self.username.errors.append('Unknown username.')
            return False
        # valid password?
        if not self.user.compare_password(self.password.data):
            self.user = None
            self.password.errors.append('Invalid password.')
            return False
        # successfully verified
        return True
            
   


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
