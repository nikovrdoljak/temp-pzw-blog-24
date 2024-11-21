from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField, RadioField, DateField, FileField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed
from datetime import datetime

class BlogPostForm(FlaskForm):
    title = StringField('Naslov', validators=[DataRequired(), Length(min=5, max=100)])
    content = TextAreaField('Sadržaj', render_kw={"id": "markdown-editor"})
    author = StringField('Autor', validators=[DataRequired()])
    status = RadioField('Status', choices=[('draft', 'Skica'), ('published', 'Objavljeno')], default='draft')
    date = DateField('Datum', default=datetime.today)
    tags = StringField('Oznake', render_kw={"id": "tags"})
    image = FileField('Blog Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Samo slike!')])
    submit = SubmitField('Spremi')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Zaporka', validators=[DataRequired()])
    remember_me = BooleanField('Ostani prijavljen')
    submit = SubmitField('Prijava')

class RegisterForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(3, 64), Email()])
    password = PasswordField('Zaporka', validators=[DataRequired(), EqualTo('password2', message='Zaporke moraju biti jednake.')])
    password2 = PasswordField('Potvrdi zaporku', validators=[DataRequired()])
    submit = SubmitField('Registracija')
