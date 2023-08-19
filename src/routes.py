from flask import Blueprint, request, jsonify
from src.database import character_schema, User
from flask_cors import CORS, cross_origin
from src.constants.http_status_codes import *
import math
from flasgger import swag_from

character_bp = Blueprint('character_bp', __name__)
CORS(character_bp)

@character_bp.get('/')
@cross_origin()
@swag_from('./docs/search.yaml')
def character():
    try:
        char_name = request.args.get('name', '')
        char_page = request.args.get('page', 1)

        try:
            char_page = int(char_page)
        except ValueError:
            search_result = {
                'data':{
                    'success': False,
                    'error': 'Invalidpage number. Please enter a valid integer'
                },
                'http_code': HTTP_400_BAD_REQUEST
            }
        
            return jsonify(search_result.get('data')), HTTP_400_BAD_REQUEST
        
        character_count = User.query.filter(User.name.ilike(f'%{char_name}%')).count()

        if not character_count:
            search_result = {
                'data':{
                    'success': False,
                    'error': 'No characters found with the given page.'
                },
                'http_code': HTTP_404_NOT_FOUND
            }

        total_pages = math.ceil(character_count/20)

        if(char_page>total_pages):
            search_result = {
                'data': {
                    'success': False,
                    'error': 'Page number out of range.'
                },
                'http_code': HTTP_404_NOT_FOUND
            }
            return jsonify(search_result.get('data')), HTTP_404_NOT_FOUND 

        query = User.query.filter(User.name.ilike(f'%{char_name}%')).order_by(User.id.asc()).paginate(page = int(char_page), per_page = 20)

        query_data = character_schema.dump(query.items)

        search_result = {
            'data': {
                    'success' : True,
                    'page' : query.page,
                    'total_pages' : query.pages,
                    'results' : query_data
                },
                'http_code': HTTP_200_OK
        }

        return jsonify(search_result.get('data')), HTTP_200_OK
    
    except Exception as e:
        raise