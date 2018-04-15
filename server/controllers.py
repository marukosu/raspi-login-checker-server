from datetime import datetime

from flask import Blueprint, jsonify, request, make_response, abort

from .models import Login, User

app = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)


@app.route('/logins', methods=['POST'])
def register_login():
    if not request.json or 'idm' not in request.json or 'ts' not in request.json:
        abort(400)

    login = Login.create(datetime.fromtimestamp(request.json['ts']))
    login.relate_user_by_idm(request.json['idm'])

    return jsonify({'message': 'ok'})


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404)

    return jsonify(user.to_json())


@app.route('/users/', methods=['GET'])
def get_users():
    users = User.query.all()
    if users is None:
        abort(404)

    return jsonify({'users': [user.to_json() for user in users]})


@app.route('/users/', methods=['POST'])
def create_user():
    if not request.json or 'username' not in request.json:
        abort(400)
    User.create(request.json['username'])

    return jsonify({'message': 'ok'})


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404)

    if not request.json or 'username' not in request.json:
        abort(400)

    user.update(request.json['username'])

    return jsonify({'message': 'ok'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404)

    user.delete()

    return jsonify({'message': 'ok'})


@app.app_errorhandler(400)
def handle_400(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.app_errorhandler(404)
def handle_404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
