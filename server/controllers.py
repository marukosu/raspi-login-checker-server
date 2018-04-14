from datetime import datetime

from flask import Blueprint, jsonify, request, make_response, abort

from .models import Login

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


@app.app_errorhandler(400)
def handle_400(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.app_errorhandler(404)
def handle_404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
