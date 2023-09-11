"""User's API Resource"""

from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from ..repositories.user import UserRepository

# Create JSON data
user_post_args = reqparse.RequestParser()
user_post_args.add_argument('phone_number', type=int, help='Phone number required')
user_post_args.add_argument('username', type=str, help='Username required')
user_post_args.add_argument('dot', type=str, help='Date of birth required')
user_post_args.add_argument('gender', type=str, help='Gender required')

resource_field = {
    'id': fields.Integer,
    'phone_number': fields.Integer,
    'username': fields.String,
    'dot': fields.String,
    'gender': fields.String,
}

class UserAPI(Resource):

    @marshal_with(resource_field)
    def post(self, id):
        args = user_post_args.parse_args()
        user = UserRepository.add_user(id=id, args=args)
        return user, 201