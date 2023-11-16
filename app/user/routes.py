from app.user import bp
from flask import request, render_template, current_app, url_for, redirect, flash
from flask_login import current_user
from app.models import User

@bp.route('/usuarios')
def usuarios():
  if not current_user.is_authenticated:
    flash('Página restrita, faça login para acessá-la')
    return redirect(url_for('auth.entrar', next=url_for('user.usuarios')))
    
  page = request.args.get('page', 1, type=int)
  usuarios = User.query.order_by(User.created.desc()).paginate(page=page, per_page=current_app.config['PER_PAGE'], error_out=False)
  next_url = url_for('user.usuarios', usuarios.next_num) if usuarios.has_next else None
  prev_url = url_for('user.usuarios', usuarios.prev_num) if usuarios.has_prev else None
  return render_template(
    'user/usuarios.html',
    title='Usuários',
    usuarios=usuarios.items,
    next_url=next_url,
    prev_url=prev_url)