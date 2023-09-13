import sys
import os
# Insert project root path to sys.path
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, PROJECT_PATH)

from flask import Flask
from api.routes.auth import auth

def create_app():
    app = Flask(__name__)

    # Registering blueprints
    app.register_blueprint(auth)


    app.run(debug=True)