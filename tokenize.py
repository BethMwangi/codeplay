
from itsdangerous import URLSafeTimedSerializer
from token import *

def generate_confirmation_token(email):
	serializer = URLSafeTimedSerializer('secret_key')
	return serializer.dumps(email, salt=('SECURITY_PASSWORD_SALT'))

def confirm_token(token, expiration=3600):
	serializer = URLSafeTimedSerializer('secret_key')
	try:
		email=serializer.loads(
			token,
			salt='SECURITY_PASSWORD_SALT',
			max_age=expiration
			)
	except:
		return False
	return email
	
