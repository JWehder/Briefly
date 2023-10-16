from flask import request, session, jsonify, send_file, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
import traceback
from functools import wraps
from config import app, db, api
from models import User
from config import Flask, SQLAlchemy, db
from logic import convert_text_to_voice, send_email

# HTTP Constants
HTTP_SUCCESS = 200
HTTP_CREATED = 201
HTTP_NO_CONTENT = 204
HTTP_UNAUTHORIZED = 401
HTTP_NOT_FOUND = 404
HTTP_BAD_REQUEST = 400
HTTP_CONFLICT = 409
HTTP_SERVER_ERROR = 500
HTTP_UNPROCESSABLE_ENTITY = 422

def authorized(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return make_response(jsonify({'error': 'Not authorized'}), HTTP_UNAUTHORIZED)
        return func(*args, **kwargs)
    return wrapper
