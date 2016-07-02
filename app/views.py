from app import app
from flask import Flask, render_template, request, flash, session, url_for, redirect
from functools import wraps
from forms import SignupForm
from models import db, User
#from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)
#db = SQLAlchemy(app)


@app.route('/')
def homepage(): 
    return "An app that greats u daily"



#login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash ('You need to login first.')
            return redirect(url_for('login'))
        return wraps

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
			newuser = User(form.username.data, form.email.data, form.password.data)
			db.session.add(newuser)
			db.session.commit()

			session['email'] = newuser.email
			return redirect(url_for('home'))
    elif request.method == 'GET':
		    return render_template('signup.html', form=form)

