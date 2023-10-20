from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from datetime import datetime

db = SQLAlchemy()
ma = Marshmallow()

class Character(db.Model):
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


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)


class CharacterSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "status", "species", "type_char", "gender", "origin_name", "location_name", "image")

class UserSchema(ma.Schema):
    class Meta:
        fields = ("uid", "first_name", "last_name", "email")

character_schema = CharacterSchema(many=True)
user_schema = UserSchema()