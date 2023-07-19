from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/RickAndMorty'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type_char = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    origin_name = db.Column(db.String(50), nullable=False)
    location_name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)



class CharacterSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "status", "species", "type_char", "gender", "origin_name", "location_name", "image")


character_schema = CharacterSchema(many=True)


@app.route('/character', methods=['GET'])
def character():
    char_name = request.args.get('name', '')
    char_page = request.args.get('page', 1)

    query = User.query.filter(User.name.ilike(f'%{char_name}%')).order_by(User.id.asc()).paginate(page = int(char_page), per_page = 20)

    return jsonify({
        'page' : query.page,
        'total_pages' : query.pages,
        'results' : character_schema.dump(query.items)
    }), 200
  


if __name__ == '__main__':
    app.run(debug=True)