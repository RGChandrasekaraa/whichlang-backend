from flask import Flask
from flask_cors import CORS
from .routes import main_routes


def create_app():
    app = Flask(__name__)
    # Enable CORS for all routes and origins
    CORS(app)
    app.register_blueprint(main_routes)
    return app
