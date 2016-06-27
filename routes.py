from flask import Flask,url_for, request, render_template,session, redirect
from app import app, mongo
import bcrypt

# creating route for first page
@app.route('/')
def index():
    # check if username is in session object
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    # when there is no username in the session
    return render_template('index.html')


# creating route for login
@app.route('/login', methods = ['POST'])
def login():
    # collection for the database
    users = mongo.db.users
    # find the login name in the database
    login_user = users.find_one({'name' : request.form['username']})
    # condition for when the login_user exists
    if login_user:
        # comparing passwords
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            # add user to the session
            session['username'] = request.form['username']
            return redirect(url_for ('index'))
    # if login_user doesnt exist or password is wrong
    return 'Invalid username/password combination'

