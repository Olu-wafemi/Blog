from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,EqualTo
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
   
    confirm_password = PasswordField('Confirm_Password',validators=[DataRequired()])

    
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    
   
   
   

    
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('password')])
    remember =  BooleanField('Remember Me')
    submit = SubmitField('Login')