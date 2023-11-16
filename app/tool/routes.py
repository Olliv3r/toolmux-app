from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.tool import bp
from app.models import Tool
from app.tool.forms import RegisterToolForm
from app import db

@bp.route('/ferramentas')
def ferramentas():
  if not current_user.is_authenticated:
    flash('Página restrita, faça login para acessá-la')
    return redirect(url_for('auth.entrar', next=url_for('tool.ferramentas')))
    
  tool = Tool.query.all()
  return render_template('tool/ferramentas.html', title='Ferramentas', tools=tool)
  
@bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
  if not current_user.is_authenticated:
    flash('Página restrita, faça login para accesá-la')
    return redirect(url_for('auth.entrar', next=url_for('tool.cadastrar')))
    
  form = RegisterToolForm()
  
  if form.validate_on_submit():
    tool = Tool(
      name=form.name.data,
      author=form.author.data,
      alias=form.alias.data,
      custom_alias=form.custom_alias.data,
      name_repo=form.name_repo.data,
      type_install=form.type_install.data,
      category=form.category.data,
      dependencies=form.dependencies.data
    )
    db.session.add(tool)
    db.session.commit()
    flash('Ferramenta registrada com sucesso')
    return redirect(url_for('tool.ferramentas'))
  
  return render_template('tool/cadastrar.html', title='Cadastrar', form=form)