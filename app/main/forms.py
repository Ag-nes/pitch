from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import input_required, Email


# pictch form section
class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField(u'Pitch Category',
                           choices=[('coding', 'coding'), ('life', 'life'),('educational', 'educational')])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')


# comment form section
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')


# update profile

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please tell us about yourself', validators=[input_required()])
    submit = SubmitField('Submit')