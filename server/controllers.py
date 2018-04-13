from flask import Blueprint, jsonify, make_response

app = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)

@app.route('/index')
def index():
    return jsonify({'message': 'Hello world'})

@app.app_errorhandler(404)
def handle_404(error):
    return make_response(jsonify({'error': 'Not found'}), 404)