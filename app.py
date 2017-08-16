from flask import Flask

# todo import logging

# import configs
DEBUG = True

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SRSS4Life'
