import sys
import os
# Insert project root path to sys.path
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, PROJECT_PATH)

from flask import Flask, jsonify, request
from app.models.user import User
from app.controllers.orm import create_user
from app.database import session

def create_app():
    app = Flask(__name__)

    # registration route
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        # Take json data
        data = request.json

        #Create new user
        new_user = User(
            phone_number=data['phone_number'],
            facebook_account=data['facebook_account'],
            google_account=data['google_account'],
            username=data['username'],
            dot=data['dot'],
            gender =data['gender'],
            singles_skill=data['singles_skill'],
            doubles_skill=data['doubles_skill'],
            club=data['club']
        )

        create_user(session=session, user=new_user)

        return jsonify(
                message="Successfully created user",
                status=200
            )

    app.run(debug=True)
    return app