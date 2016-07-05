import os
from app import app
from flask import Flask, render_template, request, flash, g, session, url_for, redirect
from functools import wraps
#from app.forms import SignupForm 
from forms import LoginForm
#from models import db, User
from app import db
from flask.ext.login import login_required
#from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)
#db = SQLAlchemy(app)
#app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    return wrap
    
  
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        return redirect('/login')
        # Login and validate the user.
       
    
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form = form)    
    
#signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #posting method
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

