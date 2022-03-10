from flask import render_template
from . import main

@main.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    error = "We could not load the page you requested for. Check the url and try again!!!"
    return render_template('error.html'),404