from flask import Flask

app = Flask(__name__)
app.config ['SQLACHEMY_DATABASE_URI'] = 'postresql://codeplay:codeplay'