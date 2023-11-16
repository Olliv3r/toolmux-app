from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, logout_user, current_user
from app.auth import bp
from app import db
from app.auth.forms import LoginForm, RegisterForm, UserEdit
from app.models import User

@bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
  if current_user.is_authenticated:
    return redirect(url_for('main.inicio'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Usuário e/ou senha inválido')
      page_next = request.args.get('next') != None or url_for('auth.entrar')
      return redirect(page_next)
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next') or url_for('main.inicio')
    return redirect(next_page)
  return render_template('auth/entrar.html', form=form, title='Entrar')
 
@bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
  if current_user.is_authenticated:
    return redirect(url_for('main.inicio'))
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(name=form.name.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Usuário cadastrado com sucesso')
    return redirect(url_for('auth.entrar'))
  return render_template('auth/registrar.html', title='Registrar', form=form)
  
@bp.route('/profile', methods=['GET', 'POST'])
def profile():
  if not current_user.is_authenticated:
    flash('Página restrita, faça login para acessá-la')
    return redirect(url_for('auth.entrar', next=url_for('auth.profile')))

  form = UserEdit()
  if request.method == 'GET':
    form.name.data = current_user.name
    form.email.data = current_user.email
  elif form.validate_on_submit():
    current_user.name = form.name.data
    current_user.email = form.email.data
    current_user.set_password(form.password.data)
    db.session.commit()
    flash('Perfil atualizado com sucesso')
  return render_template('auth/profile.html', title='Perfil', form=form)
  
@bp.route('/sair')
def sair():
  if not current_user.is_authenticated:
    flash('Ja está deslogdo')
    return redirect(url_for('main.inicio'))
    
  logout_user()
  flash('Saiu')
  return redirect(url_for('auth.entrar'))