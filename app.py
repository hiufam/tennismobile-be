import sys
import os
# Insert project root path to sys.path
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, PROJECT_PATH)

from flask import Flask
from flask.blueprints import Blueprint
import api.routes

def create_app():
    app = Flask(__name__)

    # Registering blueprints
    for blueprint in vars(api.routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)


    app.run(debug=True)