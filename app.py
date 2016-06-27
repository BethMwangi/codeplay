# This script runs the allication using a development server

# creating flask object

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo

app = Flask(__name__)
# setting up Bcrypt
bcrypt = Bcrypt(app)
# adding Pymongo
mongo = PyMongo(app)

# making the WSGI interface accessible at top level
wsgi_app = app.wsgi_app

# import all of our routes from routes routes.py

from routes import *

# Launching our server

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
