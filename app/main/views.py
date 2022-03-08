from . import main
from flask import render_template
from flask_login import login_required

@main.route("/")
def index():

    header = 'Where are your personal pitches?'

    return render_template('index.html', header = header)

@main.route('/pitches', methods = ['GET','POST'])
@login_required
def new_review():


    return render_template('pitches.html',)

