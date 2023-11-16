from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

type_install = ['apt', 'git']
categories = [
    "Information Collection",
    "Vulnerability Analysis",
    "Wireless Attacks",
    "Web Applications",
    "Sniffing and Faking",
    "Maintaining Access",
    "Reporting Tools",
    "Exploitation Tools",
    "Forensic Tools",
    "Stress Test",
    "Password Attacks",
    "Reverse Engineering",
    "Hardware Hacking",
    "Extra"
]

class RegisterToolForm(FlaskForm):
  name = StringField('Nome', validators=[DataRequired()])
  author = StringField('Autor', validators=[DataRequired()])
  alias = StringField('Apelido')
  custom_alias = StringField('Apelido customizado')
  name_repo = StringField('Nome do repositório')
  type_install = SelectField('Instalaçã via', choices=type_install, default='apt', validators=[DataRequired()])
  category = SelectField('Categoria', choices=categories, default='Extra', validators=[DataRequired()])
  dependencies = StringField('Dependencias')
  submit = SubmitField('Cadastrar')