from . import db
# from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
# from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'


    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'