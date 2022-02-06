from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import input_required,Email,EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[input_required(),Email()])
    password = PasswordField('Password',validators =[input_required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

# registration form
class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[input_required(),Email()])
    author = StringField('Enter authors name',validators = [input_required()])
    password = PasswordField('Password',validators = [input_required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [input_required()])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('This account exists')

    def validate_author(self,data_field):
        if User.query.filter_by(author = data_field.data).first():
            raise ValidationError('That author name is taken')
