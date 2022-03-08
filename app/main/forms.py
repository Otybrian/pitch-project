from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Say more about you so we know you better',validators = [DataRequired()])
    submit = SubmitField('Submit')
