from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

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