from flask import render_template, jsonify, request
from app import app, db
import json

from models import transfer
# from hardware_utils import linux_hardware
# from weather_utils import meteye
from api import nci, pawsey


@app.route('/')
def hello_world():
    app.logger.debug('Rendering home page')
    return render_template('index.html')


@app.route('/sentinel/<sentinel_num>/table/<date>')
def render_nci_table(sentinel_num, date):
    """

    :param sentinel_num:
    :param date:
    :return:
    """
    from api.nci.get_results_from_sara import get_nci_url_published_after
    quicklook_list = []

    return_list = get_nci_url_published_after(sentinel_num, date)

    for item in return_list:
        quicklook_list.append(item.replace('.zip', '.png'))

    return render_template('table.html', table=return_list, quicklook=quicklook_list)


@app.route('/table')
def render_table():
    """

    :return:
    """
    return_list = []
    u = transfer.User.query.all()

    for item in u:
        return_list.append([item.nickname, item.email])

    return render_template('table.html', table=return_list)


@app.route('/get_test_nci')
def get_test_nci():
    from api.nci.get_results_from_sara import get_by_date

    result = get_by_date('2017-10-29', '2017-11-01', 2)

    return jsonify(result)


@app.route('/get_published_after_test')
def get_published_after_test():
    from api.nci.get_results_from_sara import get_published_after

    result = get_published_after('2017-10-31', 2)

    breakpoint = 'break'

    # result = json.load(result)

    return jsonify(result)


@app.route('/sentinel/<sentinel_num>/get_published_after/<date>')
def get_published_after(sentinel_num, date):
    """

    :param sentinel_num:
    :param date:
    :return:
    """
    from api.nci.get_results_from_sara import get_published_after

    result = get_published_after(sentinel_num, date)

    return jsonify(result)


@app.route('/map')
def return_map():
    return render_template("map.html")


@app.route('/sentinel/<sentinel_num>/get_nci_url_published_after/<date>')
def get_nci_url_published_after(sentinel_num, date):
    """

    :param sentinel_num:
    :param date:
    :return:
    """
    from api.nci.get_results_from_sara import get_nci_url_published_after

    result = get_nci_url_published_after(sentinel_num, date)

    return jsonify(result)
