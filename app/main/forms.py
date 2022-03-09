from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Say more about you so we know you better',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Categories', choices=[('Self', 'Self Pitches'), ('Interview', 'Interview Pitches'),
               ('Product', 'Product Pitches'), ('Promotion', 'Promition Pitches'), ('Job Experience', 'Job Experience Pitches'), 
               ('Education', 'Education Background Pitches')], validators=[DataRequired()])
    post = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')
