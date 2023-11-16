from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Senha', validators=[DataRequired()])
  remember_me = BooleanField('Lembrar de Mim')
  submit = SubmitField('Acessar')
  
class RegisterForm(FlaskForm):
  name = StringField('Nome', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Senha', validators=[DataRequired()])
  password2 = PasswordField('Senha', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Cadastrar')
  
class UserEdit(FlaskForm):
  name = StringField('Nome', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Senha', validators=[DataRequired()])
  submit = SubmitField('Editar')