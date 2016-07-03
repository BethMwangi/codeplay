
# This script runs the allication using a development server

# creating flask object

from flask import Flask
from app import app


if __name__ == '__main__':
    app.secret_key = 'mysecret'

    app.run(debug=True)


