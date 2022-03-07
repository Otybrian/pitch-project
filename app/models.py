from . import db
from flask_login import UserMixin



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String)



    def __repr__(self):
        return f'User {self.username}'