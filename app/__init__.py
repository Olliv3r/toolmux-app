from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask_moment import Moment
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap5()
login = LoginManager()
login.login_view = 'auth.entrar'
login.login_message = 'Página restrita, faça login para ter acesso'
moment = Moment()

def create_app(class_config=Config):
  app = Flask(__name__)
  app.config.from_object(class_config)
  db.init_app(app)
  migrate.init_app(app, db)
  bootstrap.init_app(app)
  login.init_app(app)
  moment.init_app(app)
  
  # rotas de auth
  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp, prefix='/auth')
  # Rotas de main
  from app.main import bp as main_bp
  app.register_blueprint(main_bp)
  # Rotas de tool
  from app.tool import bp as tool_bp
  app.register_blueprint(tool_bp)
  # Rotas de comunidade
  from app.comunidade import bp as comunidade_bp
  app.register_blueprint(comunidade_bp)
  # Rotas de user
  from app.user import bp as user_bp
  app.register_blueprint(user_bp)
  
  return app
from app import models