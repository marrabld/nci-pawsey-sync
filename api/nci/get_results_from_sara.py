from auscophub import saraclient


def get_by_date(start_date, completion_date, sentinel_number):
    """

    :param start_date:
    :param completion_date:
    :param sentinel_number:
    :return:
    """
    url_opener = saraclient.makeUrlOpener()
    sentinel = sentinel_number
    param_list = ['startDate={}'.format(start_date), 'completionDate={}'.format(completion_date)]
    results = saraclient.searchSara(url_opener, sentinel, param_list)

    return results


def get_published_after(sentinel_number, published_date):
    """

    :param sentinel_number:
    :param published_date:
    :return:
    """
    url_opener = saraclient.makeUrlOpener()
    sentinel = sentinel_number
    param_list = ['publishedAfter={}'.format(published_date)]
    results = saraclient.searchSara(url_opener, sentinel, param_list)

    return results


def get_nci_url_published_after(sentinel_number, published_date):
    """

    :param published_date:
    :param sentinel_number:
    :return:
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
