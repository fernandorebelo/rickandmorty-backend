from flask import Flask
from src.database import db, ma
from src.routes import CORS, character_bp
#from flask_restplus import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/RickAndMorty'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init the database
db.init_app(app)
ma.init_app(app)
CORS(app)

# Register blueprints
app.register_blueprint(character_bp, url_prefix='/character')