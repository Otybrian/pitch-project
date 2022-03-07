from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')


    def __repr__(self):
        return f'User {self.name}'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You are not authorized to read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'




    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    _tablename__ = 'pitches'
    id = db.Column(db.Integer)
    category = db.Column(db.Text)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('PostLike', backref = 'post', lazy = 'dynamic')
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(id = id).all()
        return pitches

    def __repr__(self):
        
        return f"Pitch('{self.category}','{self.title}', '{self.content}','{self.date_posted}', '{self.user_id}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    pitches_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    pitches_content = db.Column(db.String, db.ForeignKey('pitches.content'))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(post_id = id).all()

        return comments


    def __repr__(self):
        return f"Comment('{self.comment}', '{self.date_posted}', '{self.user_id}'')"


class CommentLike(db.Model,):
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, ForeignKey('users.username'))
    post_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment_like  = db.relationship ('User', backref = 'users')

    def save_like(self):
        db.session.add(self)
        db.session.commit()

        return CommentLike
