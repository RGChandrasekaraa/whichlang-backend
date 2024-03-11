from flask import Blueprint, request, jsonify
from flask import current_app as app
from werkzeug.exceptions import BadRequest
from .utils import detect_language

main_routes = Blueprint('main', __name__)


@main_routes.route('/detect_language', methods=['POST'])
def language_route():
    try:
        # Ensure JSON is valid
        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({'error': 'Invalid JSON'}), 400

        # Check if 'text' is present in the JSON
        text = data.get('text')
        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Perform language detection
        language = detect_language(text)
        return jsonify({'language': language})

    except Exception as e:
        app.logger.error(f'Unexpected error: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500

# Custom error handler for 404 Not Found


@main_routes.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404
