from flask import render_template, jsonify, request
from app import app, db

from models import transfer
#from hardware_utils import linux_hardware
#from weather_utils import meteye
from api import nci, pawsey


@app.route('/')
def hello_world():
    app.logger.debug('Rendering home page')
    return render_template('index.html')

@app.route('/table')
def render_table():

    return_list = []
    u = transfer.User.query.all()

    for item in u:
        return_list.append([item.nickname, item.email])

    table = jsonify(return_list)

    return(render_template('table.html'))



# @app.route('/blk_devices')
# def get_blk_devices():
#     response = linux_hardware.get_blk_devies()
#     return render_template('hardware.html', response=response)
#
#
# @app.route('/hardware')
# def get_hardware():
#     response = linux_hardware.get_hardware()
#     return response
#
#
# @app.route('/api/v0/dev/<string:device>')
# def get_disk(device):
#     response = linux_hardware.get_device_size(device)
#
#     if len(response) == 0:
#         return "<strong>No such device \"{}\" </strong>".format(device)
#     else:
#         return jsonify(response)
#
#
# @app.route('/api/v1/weather', methods=['GET'])
# def get_weather():
#     location = request.args['location']
#
#     response = meteye.get_weather(location, time=None)
#     return jsonify(response)
