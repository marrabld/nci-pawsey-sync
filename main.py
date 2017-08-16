"""
This is the main entry point of the application
"""
from app import app, DEBUG
from views import *


if __name__ == '__main__':
    if DEBUG:
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run()

