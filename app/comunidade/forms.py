from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ComunidadeForm(FlaskForm):
  body = TextAreaField('Sugestão', validators=[DataRequired()])
  submit = SubmitField('Publicar')