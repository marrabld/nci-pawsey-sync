import app
from app import db
from models import transfer
import datetime
from app import config
import requests
import shutil
import os
from app import app

def download_and_cache_images(remote_file_list):
    """
    Download from the NCI all the images in the list.  Cache them locally for push to Pawsey

    :param remote_file_list:
    :return:
    """

    cache = config.get('DEV', 'cache')

    for url in remote_file_list:
        app.logger.debug('Downloading :: '.format(url))

        # ------------------------------#
        # We want to preserve the folder structure.
        # We can build it from the URL itself.
        # ------------------------------#


        # figure out our directory structure
        sub_url = url.split('data')[1]

        path, file = os.path.split(sub_url)

        # append our cache directory
        local_path = os.path.join(cache, path[1:])  # drop the '/'
        print(cache)

        print(local_path)
        # create the directories if they don't exist.

        try:
            os.makedirs(local_path)
        except:
            pass

        file_name = os.path.join(local_path, file)

        from requests import get  # to make GET request

        with open(file_name, "wb") as f:
            # get request
            response = get(url)
            # write to file
            f.write(response.content)

        # This is the Python 3 way.   TODO fix me for Python 2

        # Download the file from `url` and save it locally under `file_name`:
        # with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        #   shutil.copyfileobj(response, out_file)


def get_last_sync(successful=True):
    """
    Query the database and ask when was the last time we tried to sync

    :param successful:  If set to True, we ask when was the last successful sync
    :return:
    """

    schedule = transfer.Schedule.query.all()

    result = str(schedule[-1].date_time)

    # ==============================#
    # we step backwards through our list until we find a pair
    # ==============================#
    if successful:
        done = False
        i_iter = -1
        while not done:
            if schedule[i_iter].transfer_success:
                result = str(schedule[i_iter].date_time)
                done = True
            else:
                i_iter -= 1

    return result


def sync_nci_to_pawsey(sentinel=2):
    """
    Grab a list of files since our last successful sync and push them to Pawsey

    :param sentinel: The satellite number
    :return:
    """

    last_sync = get_last_sync()

    from api.nci.get_results_from_sara import get_published_after

    last_published = get_published_after(sentinel_number=sentinel, published_date=last_sync.split(' ')[0])

    # ==============================#
    # now push to pawsey
    # ==============================#

    # TODO

    # ------------------------------#
    # Now we update the database
    # ------------------------------#

    pawsey_success = True

    pi = config.get('DEV', 'principle_investigator')

    # ------------------------------#
    # we need to trim the data
    # ------------------------------#

    if len(last_sync) >= 20:
        # chop = len(last_sync.split()[-1]) - 4
        last_sync = last_sync[:19]

    # _last_sync = parse(last_sync)
    last_sync = datetime.datetime.strptime(last_sync, '%Y-%m-%d %H:%M:%S')
    # last_sync = datetime.datetime()

    date = datetime.datetime.now()
    if pawsey_success:
        s = transfer.Schedule(date_time=date,
                              pi=pi,
                              last_published_date=last_sync,
                              transfer_success=True)
        db.session.add(s)

    db.session.commit()

    return True
