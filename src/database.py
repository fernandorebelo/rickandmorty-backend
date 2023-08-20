from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from datetime import datetime


db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type_char = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=False)
    origin_name = db.Column(db.String(50), nullable=False)
    location_name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)



class CharacterSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "status", "species", "type_char", "gender", "origin_name", "location_name", "image")


character_schema = CharacterSchema(many=True)

""" class ExceptionTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    error_message = db.Column(db.String(1000), nullable=False)
    request_headers = db.Column(db.JSON, nullable=True)
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    endpoint = db.Column(db.String(255), nullable=True)
    http_method = db.Column(db.String(10), nullable=True)
    traceback = db.Column(db.Text, nullable=True)

class SearchLogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    request_headers = db.Column(db.JSON, nullable=True)
    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    endpoint = db.Column(db.String(255), nullable=True)
    success = db.Column(db.Boolean, nullable = False)
    search_result_cached = db.Column(db.Boolean, nullable = False)
    status_code = db.Column(db.Integer, nullable = False) """