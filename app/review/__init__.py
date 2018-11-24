from flask import Blueprint

review = Blueprint('review',__name__,template_folder='templates')

from app.review import routes