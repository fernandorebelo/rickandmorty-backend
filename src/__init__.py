from flask import Flask, jsonify
from src.database import db, ma
from src.routes import CORS, character_bp
from flasgger import Swagger
from src.constants.http_status_codes import *
from src.utils.exception_tracker_log import log_exception


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/RickAndMorty'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    'title':'Rick and Morty backend API',
    'uiversion': 1
}

# Init the database
db.init_app(app)
ma.init_app(app)
CORS(app)

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