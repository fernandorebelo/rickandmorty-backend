from flask import Flask, jsonify
from src.database import db, ma
from src.routes import CORS, character_bp
from flasgger import Swagger
from src.config.swagger import template, swagger_config
from src.constants.http_status_codes import *
from src.utils.exception_tracker_log import log_exception


app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'SECRET_KEY',
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/RickAndMorty',
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

@app.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
  return jsonify({'error': 'page not found'}), HTTP_404_NOT_FOUND

@app.errorhandler(Exception)
def handle_exceptions(e):
  log_exception(e)
  return jsonify({
      'success': False,
      'error': 'Something bad happened, please try again'
  }), HTTP_500_INTERNAL_SERVER_ERROR