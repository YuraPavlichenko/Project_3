from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Such username already exists! Try another one")


    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError("Such email already exists! Try another one")

    username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name: ', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')


class AddItemForm(FlaskForm):
    name = StringField(label='Item name')
    price = IntegerField(label='Item price')
    barcode = IntegerField(label='Item barcode')
    description = StringField(label='Item description')
    submit = SubmitField(label='Add Item')