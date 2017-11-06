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
    param_list = ['publishedAfter={}'.format(published_date)]
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
