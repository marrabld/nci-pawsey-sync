from app import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nickname = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#
#     def __repr__(self):
#         return '<User %r>' % (self.nickname)
#
#     def as_dict(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}


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
