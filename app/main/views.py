from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from ..models import User

@main.route("/")
def index():

    header = 'Where are your personal pitches?'

    return render_template('index.html', header = header)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def new_review():


    return render_template('pitches.html',)

