from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    fullname = StringField('Full Name', validators=[DataRequired(), Length(min=3, max=30)])
    address = StringField('Address', validators=[DataRequired(), Length(min=7, max=50)])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class OrderIDForm(FlaskForm):
    order_id = StringField('Order ID', validators=[DataRequired()])
    submit = SubmitField('Track')

class ReserveForm(FlaskForm):
    submit = SubmitField('Reserve')

class AddForm(FlaskForm):
    submit = SubmitField('Add')

class OrderForm(FlaskForm):
    submit = SubmitField('Order Now')
