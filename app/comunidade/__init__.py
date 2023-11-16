from flask import Blueprint

bp = Blueprint('comunidade', __name__)

from app.comunidade import routes