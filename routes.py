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

