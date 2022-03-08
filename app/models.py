# from unicodedata import category
from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'


    

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You are not able to read the password attribute')    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
        

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    post = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls, id):
        posts = Post.query.filter_by(id = id).all()
        return posts


    def __repr__(self):
        return f"Post ('{self.title}', '{self.post}', '{self.posted_date}')"

class Reaction(db.Model):
    __tablename__ = 'reactions'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)


    def save_reaction(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_reaction(cls, id):
        reaction = Reaction.query.filter_by(post_id = id).all()
        return reaction


    def __repr__(self):
        return f"Reaction('{self.comment}', '{self.posted_date}')"

