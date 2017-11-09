from app import db
from models import transfer
import datetime
from dateutil.parser import parse


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

    :return:
    """

    from app import config
    last_sync = get_last_sync()

    from api.nci.get_results_from_sara import get_published_after

    last_published = get_published_after(sentinel_number=sentinel, published_date=last_sync.split(' ')[0])

    #==============================#
    # now push to pawsey
    #==============================#

    # TODO

    #------------------------------#
    # Now we update the database
    #------------------------------#

    pawsey_success = True
    
    pi = config.get('DEV', 'principle_investigator')

    #------------------------------#
    # we need to trim the data
    #------------------------------#

    if len(last_sync) >= 20:
        #chop = len(last_sync.split()[-1]) - 4
        last_sync = last_sync[:19]

    #_last_sync = parse(last_sync)
    last_sync = datetime.datetime.strptime(last_sync, '%Y-%m-%d %H:%M:%S')
    #last_sync = datetime.datetime()

    date = datetime.datetime.now()
    if pawsey_success:
        s = transfer.Schedule(date_time=date,
                              pi=pi,
                              last_published_date=last_sync,
                              transfer_success=True)
        db.session.add(s)

    db.session.commit()

    return True

