from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError

class RegistrationForm(FlaskForm):
    name = StringField('What\'s your name?',validators = [DataRequired(),Length(3,50,message = 'Should be between 3 and 25 characters')])
    email = StringField('Enter your Email',validators = [DataRequired(),Email()])
    password = PasswordField('Enter Password',validators = [DataRequired(),EqualTo('confirm',message='Paswords must match')])
    confirm = PasswordField('Confirm Password',validators = [DataRequired()])
    submit = SubmitField('Register')
