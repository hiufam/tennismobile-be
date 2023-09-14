from flask import Blueprint, request, jsonify

from ..models.user import User
from ..validation import PhoneNumberSchema

registration = Blueprint('registration', __name__, url_prefix='/api/registration')

new_user = User()

@registration.post('/phone-number')
def register_phone_number():

    errors = PhoneNumberSchema().validate(request.json)
    if errors:
        return jsonify({
            'error': errors['phone_number'][0]
        }), 400
    
    phone_number = request.json['phone_number']
    new_user.phone_number = phone_number

    return jsonify({
        'user': {
            'phone_number': phone_number
        }
    }), 200