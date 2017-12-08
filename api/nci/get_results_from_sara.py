"""
This module is a convenience wrappwer around the auscophub saraclient python module
"""

from auscophub import saraclient


def get_by_date(start_date, completion_date, sentinel_number):
    """
    Retreive a list of satellite metadata files that were collected between two dates.  Retuns json array

    :param start_date: The start date the files were collected from the sensor
    :param completion_date: The end date the files were collected from the sensor
    :param sentinel_number:
    :return: .JSON array containing all the metadata
    """
    url_opener = saraclient.makeUrlOpener()
    sentinel = sentinel_number
    param_list = ['startDate={}'.format(start_date), 'completionDate={}'.format(completion_date)]
    results = saraclient.searchSara(url_opener, sentinel, param_list)

    return results


def get_published_after(sentinel_number, published_date):
    """
    Retrieve a list of satellite metadata files that were published after a particular date.

    The published date is the date that it was made public at the NCI.  Not the date it was collected

    :param sentinel_number: The major sentinel number.  i.e. 2  not 2a
    :param published_date: The date the files were published at the NCI
    :return: .JSON array containing all the metadata
    """
    url_opener = saraclient.makeUrlOpener()
    sentinel = sentinel_number
    param_list = ['publishedAfter={}'.format(published_date)]
    results = saraclient.searchSara(url_opener, sentinel, param_list)

    return results


def get_nci_url_published_after(sentinel_number, published_date):
    """
    Retrieve a list of downloadable URLs within the WA-SA region

    :param sentinel_number: The major sentinel number.  i.e. 2  not 2a
    :param published_date: The date the files were published at the NCI
    :return: list of URLs
    """
    url_list = []
    url_opener = saraclient.makeUrlOpener()
    sentinel = sentinel_number
    param_list = ['publishedAfter={}'.format(published_date),
                  "geometry=POLYGON((92 29, 110 29, 110 6, 115 6, 115 11, 119 11, 119 22, 129.28515625 22.0, 129.3291015625 -25.7261540736202, 141.4892558125 -25.6469489161716, -150 -90, 39 -90, 39 -49, 75 -49, 75 -2, 92 -2, 92 6, 92 29))"]
    results = saraclient.searchSara(url_opener, sentinel, param_list)

    # ==============================#
    # We are going to grab the thumbnail and use it's
    # url to construct our own download url
    # ==============================#

    for item in results:
        url = item['properties']['quicklook']
        url = url.replace('.png', '.zip')
        url_list.append(url)

    return url_list
