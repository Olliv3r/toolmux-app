from flask_login import UserMixin
from app import login, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(36), nullable=False)
  email = db.Column(db.String(36), nullable=False, index=True, unique=True)
  password = db.Column(db.String(32), nullable=False)
  created = db.Column(db.DateTime, default=datetime.utcnow)
  modified = db.Column(db.DateTime, default=datetime.utcnow)
  posts = db.relationship('Post', backref='author', lazy='dynamic')
  
  def set_password(self, password):
    self.password = generate_password_hash(password)
    
  def check_password(self, password):
    return check_password_hash(self.password, password)
    
class Tool(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(36), nullable=False)
  author = db.Column(db.String(50), nullable=False)
  alias = db.Column(db.String(50), nullable=True)
  custom_alias = db.Column(db.String(50), nullable=True)
  name_repo = db.Column(db.String(50), nullable=True)
  type_install = db.Column(db.String(50), nullable=False)
  category = db.Column(db.String(50), nullable=False)
  dependencies = db.Column(db.String(50), nullable=True)
  created = db.Column(db.DateTime, default=datetime.utcnow)
  modified = db.Column(db.DateTime, default=datetime.utcnow)
  
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(500), nullable=False)
  created = db.Column(db.DateTime, default=datetime.utcnow)
  modified = db.Column(db.DateTime, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
@login.user_loader
def load_user(id):
  return User.query.get(int(id))
  
  