from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    numb = db.column(db.Integer)
    subemail = db.column(db.String)
    message = db.column(db.String)

    def __repr__(self):
        return ""
    
    def get_uid(self):
        return self.uid