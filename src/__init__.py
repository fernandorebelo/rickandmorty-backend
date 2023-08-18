from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from src.database import db, ma, character_schema, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/RickAndMorty'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
ma.init_app(app)
CORS(app)

@app.route('/character', methods=['GET'])
@cross_origin()
def character():
    char_name = request.args.get('name', '')
    char_page = request.args.get('page', 1)

    query = User.query.filter(User.name.ilike(f'%{char_name}%')).order_by(User.id.asc()).paginate(page = int(char_page), per_page = 20)

    return jsonify({
        'page' : query.page,
        'total_pages' : query.pages,
        'results' : character_schema.dump(query.items)
    }), 200