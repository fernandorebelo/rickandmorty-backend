from flask import Blueprint, request, jsonify
from src.database import  user_schema, User, db
from src.constants.http_status_codes import *

register_bp = Blueprint('register_bp', __name__)
user_bp = Blueprint('user_bp', __name__)

@user_bp.get('/user')
def user():
    try:
        user_uid = request.args.get('uid', '')
        query = User.query.filter_by(uid=user_uid)
        user_data = user_schema.dump(query.first())
        if user_data:
            response = {
                'data': {
                    'success': True,
                    'message': 'User found.',
                    'result': user_data
                },
                'http_code': HTTP_200_OK
            }
        else:
            response = {
                'data': {
                    'success': False,
                    'message': 'User not found.',
                    'user': None
                },
                'http_code': HTTP_404_NOT_FOUND
            }

        return jsonify(response), response['http_code']
    except Exception as e:
        response = {
            'data': {
                'success': False,
                'message': 'User not found.',
                'user': None
            },
            'http_code': HTTP_500_INTERNAL_SERVER_ERROR
        }
        return jsonify(response), response['http_code']

@register_bp.post('/register')
def register():
    try:
        data = request.get_json()
        new_user = User(
            uid = data['uid'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email']
            )
        db.session.add(new_user)
        db.session.commit()

        new_user_data = user_schema.dump(new_user)

        response = {
                'data': {
                    'success': True,
                    'message': 'User created successfully',
                    'user': new_user_data
                },
                'http_code': HTTP_201_CREATED
        }

        return jsonify(response), response['http_code']
    except Exception as e:
        response = {
            'data': {
                'success': False,
                'message': 'Failed to create user',
                'user': None
            },
            'http_code': HTTP_500_INTERNAL_SERVER_ERROR
        }
        return jsonify(response), response['http_code']