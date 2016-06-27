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

# creating route for register
@app.route('/register', methods = ['POST', 'GET'])
def register():
    # when the request made is a post method
    if request.method == 'POST':
        # checking if username already exist
        users = mongo.db.users
        # searching the data
        existing_user = users.find_one({'name' : request.form['username']})

        # if it finds nothing in the database go ahead and register
        if existing_user is None:
            # first hash the password before storing in database
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # inserting the user information into the users collection
            users.insert({'name': request.form['username'], 'password': hashpass})
            # creating session
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        # the return option if username already exists
        return 'That username already exists'
    return render_template('register.html')


