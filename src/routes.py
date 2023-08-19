from flask import Blueprint, request, jsonify
from src.database import character_schema, User
from flask_cors import CORS, cross_origin

character_bp = Blueprint('character_bp', __name__)
CORS(character_bp)

@character_bp.route('/', methods=['GET'])
@cross_origin()
def character():
    print('teste')
    char_name = request.args.get('name', '')
    char_page = request.args.get('page', 1)

    query = User.query.filter(User.name.ilike(f'%{char_name}%')).order_by(User.id.asc()).paginate(page = int(char_page), per_page = 20)

    return jsonify({
        'page' : query.page,
        'total_pages' : query.pages,
        'results' : character_schema.dump(query.items)
    }), 200