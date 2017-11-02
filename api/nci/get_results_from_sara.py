from auscophub import saraclient


def get_by_date(start_date, completion_date, sentinel_number):
    url_opener = saraclient.makeUrlOpener()
    sentinel = sentinel_number
    param_list = ['startDate={}'.format(start_date), 'completionDate={}'.format(completion_date)]
    results = saraclient.searchSara(url_opener, sentinel, param_list)

    return results
