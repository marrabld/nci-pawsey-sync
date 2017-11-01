#!/usr/bin/python

from flask_script import Manager, prompt_bool

import logging
import pip
from app import db
from app import app

from models import transfer

app.logger.setLevel(logging.DEBUG)

manager = Manager(app)


@manager.command
def init_db():
    """
    Initialize the database.
    :return:
    """
    app.logger.info('Initialising the application database')
    db.create_all()
    app.logger.info('Done')


@manager.command
def load_test_data():
    """
    Populate the database with dummy data so we can test the application
    :return:
    """
    if prompt_bool("Are you sure you want to continue, proceeding will drop all previous data"):
        app.logger.warning('Dropping table before generating dummy data')
        db.drop_all()
        db.create_all()

        app.logger.info("Populating database with dummy data")
        for i_iter in range(0, 20):

            u = transfer.User(nickname='john_{}'.format(i_iter), email='john_{}@email.com'.format(i_iter))
            db.session.add(u)
        db.session.commit()
        app.logger.info("Done")


@manager.command
def drop_db():
    """
    Drop the database.
    :return:
    """
    if prompt_bool("Are you sure you want to lose all your data"):
        app.logger.warning('Dropping the database, all data will be lost')
        db.drop_all()
        app.logger.warning('Done')
    else:
        app.logger.info('Skipping')


@manager.command
def update_auscop():
    """
    update the auscop api script from bitbucket
    :return:
    """
    url = "https://bitbucket.org/chchrsc/auscophub"
    cmd = "hg+"+url
    print(cmd)

    pip.main(['install', cmd])


if __name__ == "__main__":
    manager.run()
