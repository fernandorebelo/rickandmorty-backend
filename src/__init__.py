from flask import Flask, jsonify
from src.database import db, ma
from src.routes import CORS, character_bp
from flasgger import Swagger
from src.config.swagger import template, swagger_config
from src.constants.http_status_codes import *
#from src.utils.exception_tracker_log import log_exception
from src.config.automation import populate_db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'SECRET_KEY',
    SQLALCHEMY_DATABASE_URI = DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS = False,

    SWAGGER = {
         'title': 'Rick And Morty Backend Api',
         'uiversion': 3
    }
)

# Init the database
db.init_app(app)
ma.init_app(app)
CORS(app)
swager = Swagger(app)

# Register blueprints
app.register_blueprint(character_bp, url_prefix='/character')

# Ensure the database is empty
def is_database_empty():
    from src.database import User
    return db.session.query(User).count() == 0

with app.app_context():
    db.create_all()

    if is_database_empty():
      populate_db()

@app.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
  return jsonify({'error': 'page not found'}), HTTP_404_NOT_FOUND

""" @app.errorhandler(Exception)
def handle_exceptions(e):
  log_exception(e)
  return jsonify({
      'success': False,
      'error': 'Something bad happened, please try again'
  }), HTTP_500_INTERNAL_SERVER_ERROR """