from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# todo import logging
import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler

# import configs
DEBUG = True

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SRSS4Life'

##############################
# Logging info
#############################
handler = RotatingFileHandler('./logs/application.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
handler.setFormatter(Formatter('[%(asctime)s] :: %(levelname)s :: MODULE %(module)s :: lINE %(lineno)d :: %(message)s'))

app.logger.addHandler(handler)

##############################
# Set up the data base for recording when we copy and write to the database.
##############################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/test.db'  # !!! Change me on Production
db = SQLAlchemy(app)
