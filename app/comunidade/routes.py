from app.comunidade import bp
from flask import render_template, request, current_app, url_for, redirect, flash
from flask_login import current_user
from app.comunidade.forms import ComunidadeForm
from app.models import Post
from app import db

@bp.route('/comunidade', methods=['GET', 'POST'])
def comunidade():
  if not current_user.is_authenticated:
    flash('Página restrita, faça login para acessá-la')
    return redirect(url_for('auth.entrar', next=url_for('comunidade.comunidade')))
    
  form = ComunidadeForm()
  if form.validate_on_submit():
    post = Post(body=form.body.data, author=current_user)
    db.session.add(post)
    db.session.commit()
    
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.created.desc()).paginate(page=page, per_page=current_app.config['PER_PAGE'], error_out=False)
  next_url = url_for('comunidade.comunidade', page=posts.next_num) if posts.has_next else None
  prev_url = url_for('comunidade.comunidade', page=posts.prev_num) if posts.has_prev else None
  return render_template(
    'comunidade/comunidade.html', 
    title='Comunidade', 
    form=form, 
    posts=posts.items, 
    prev_url=prev_url, 
    next_url=next_url)