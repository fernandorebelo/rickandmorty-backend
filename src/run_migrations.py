from app import app
from src.database import db

with app.app_context():
    db.create_all()