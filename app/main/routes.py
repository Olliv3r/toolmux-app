from flask import (
  render_template, 
  url_for,
  redirect, 
  flash
)
from flask_login import current_user
from app.main import bp

@bp.route('/')
def inicio():
  if current_user.is_authenticated:
    return redirect(url_for('user.usuarios'))
  return render_template('main/inicio.html', title='inicio')