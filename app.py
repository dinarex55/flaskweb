from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', False)


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/api/hello', methods=['GET', 'POST'])
def hello():
    """API endpoint that returns a greeting"""
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name', 'World')
    else:
        name = request.args.get('name', 'World')
    
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'success'
    })


@app.route('/api/status', methods=['GET'])
def status():
    """API endpoint for health check"""
    return jsonify({
        'status': 'running',
        'environment': os.environ.get('FLASK_ENV', 'production')
    })


@app.route('/api/echo', methods=['POST'])
def echo():
    """API endpoint that echoes back the request data"""
    data = request.get_json()
    return jsonify({
        'echo': data,
        'received_at': str(request.remote_addr)
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not Found', 'status': 404}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal Server Error', 'status': 500}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
