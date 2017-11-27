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


class User(db.Model):
    email = db.Column(db.String(80), primary_key=True, unique=True)
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)