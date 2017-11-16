from app import db


class Schedule(db.Model):
    """
    A Table for keeping track of the scheduled data transfer
    """

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, index=True)
    # Principle Investigator
    pi = db.Column(db.String(64), index=True)
    last_published_date = db.Column(db.DateTime, index=True)
    transfer_success = db.Column(db.Boolean, index=True)
