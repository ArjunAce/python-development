from . import db
from sqlalchemy import DateTime


class TodoList(db.Model):
    __tablename__ = "todo_list"

    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    item = db.Column(db.String())
    created_at = db.Column(DateTime)
    status = db.Column(db.Boolean())
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
