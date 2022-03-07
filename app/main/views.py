from . import main
from flask import render_template


@main.route("/")
def index():

    header = 'Where are your personal pitches?'

    return render_template('index.html', header = header)
