from flask_wtf import FlaskForm # noqa
from wtforms import StringField, PasswordField, TextAreaField # noqa
from wtforms.validators import DataRequired, ValidationError, Email, Regexp, Length, EqualTo # noqa
from models import User


def name_exist(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User already exists')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('Email already exists')


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(r'^[a-zA-Z0-9_]+$'),
            name_exist
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ]
    )

    password2 = PasswordField(
        'Confirm password',
        validators=[
            DataRequired()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=4),
            EqualTo(fieldname='password2', message="Password must match")
        ]
    )


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class PostsForm (FlaskForm):
    content = TextAreaField('Whats on your mind', validators=[DataRequired()])
