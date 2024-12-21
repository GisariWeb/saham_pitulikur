from flask import Flask, Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

@api_bp.route('/hello')
def hello():
    return jsonify({'message': 'hello from api'})

@api_bp.route('/hello/<name>')
def hello_name(name):
    return jsonify({'message': f'hello from {name}'})


