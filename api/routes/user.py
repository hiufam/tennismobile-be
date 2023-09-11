from flask import Blueprint
from flask_restful import Api
from ..resources.user import UserAPI

USERS_BLUEPRINT = Blueprint('users', __name__)
# add UserAPI resource to USERS_BLUEPRINT
Api(USERS_BLUEPRINT).add_resource(UserAPI, '/users/<int:id>/')