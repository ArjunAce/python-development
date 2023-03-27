from . import db


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
