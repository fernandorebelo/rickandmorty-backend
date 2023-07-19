from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Connection, or_, select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/RickAndMorty'
db = SQLAlchemy(app)

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


    def json(self):
        return {
            'id': self.id,
            'name': self.name, 
            'status': self.status,
            'species': self.species, 
            'type_char': self.type_char,
            'gender':self.gender,
            'origin_name':self.origin_name,
            'location_name':self.location_name,
            'image':self.image
            }

def get_characters_name(name, page):

    #se estiver na pagina 1 -> offset = (valorPagina - 1) * valorLim
    limit = 20
    offset = (int(page) - 1) * limit
    query = User.query.filter(or_(User.name.ilike('%{}%'.format(name)))).order_by(User.id.asc()).limit(limit).offset(offset)
    results = [user.json() for user in query]
    return results



@app.route('/character', methods=['GET'])
def character():
    char_name = request.args.get('name', '')
    char_page = request.args.get('page', 0)
    return jsonify(get_characters_name(char_name, char_page)), 200
  


if __name__ == '__main__':
    app.run(debug=True)