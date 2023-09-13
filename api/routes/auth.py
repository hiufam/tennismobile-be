import random
from flask import Blueprint, jsonify, request
from api.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
from ..models.user import User
from ..controllers.user_controller import create_user
from ..database import session
import pyotp

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

new_user = User(
    is_verify=False
)

@auth.post('/register/phone-number')
def register_phone_number():
    phone_number = request.json['phone_number']

    if len(str(phone_number)) != 10 or not str(phone_number).isdigit():
        return jsonify({
            'error': 'Phone number is invalid'
        }), HTTP_400_BAD_REQUEST

    if session.query(User).filter(User.phone_number == phone_number).scalar() is not None:
        return jsonify({
            'error': 'Phone number is already registered'
        }), HTTP_409_CONFLICT
    
    new_user.phone_number = phone_number
    print(new_user.phone_number)

    return jsonify({
        'message': 'Required OTP to validate phone number'
    }), HTTP_200_OK

@auth.get('/otp')
def get_otp():
    if not new_user.phone_number:
        return jsonify({
            'error': 'No phone number to send OTP'
        }), HTTP_400_BAD_REQUEST
    
    # Create TOTP
    global totp 
    totp = pyotp.TOTP('base32secret3232', interval= 10)
    
    return jsonify({
            'OTP': f'{totp.now()}'
    }), HTTP_200_OK


@auth.post('/otp')
def verify_otp():
    if not new_user.phone_number:
        return jsonify({
            'error': 'No phone number to validate OTP'
        }), HTTP_400_BAD_REQUEST

    # Validate TOTP
    print(new_user.phone_number)    
    otp_code = request.json['otp_code']

    if otp_code != totp.now():
        return jsonify({
            'error': 'Invalid OTP'
        }), HTTP_400_BAD_REQUEST
    
    new_user.is_verify = True

    return jsonify({
            'error': 'Successfully validate phone number'
        }), HTTP_200_OK
    

@auth.post('/register/profile')
def register():
    register_parameters = request.json

    new_user.full_name = register_parameters['full_name']
    new_user.date_of_birth = register_parameters['date_of_birth']
    new_user.gender = register_parameters['gender']
    new_user.singles_skill = register_parameters['singles_skill']
    new_user.doubles_skill = register_parameters['doubles_skill']

    current_user = create_user(new_user)

    return jsonify({
        'id': current_user.id,
        'full_name': current_user.full_name,
        'date_of_birth': current_user.date_of_birth,
        'gender': current_user.gender,
        'singles_skill': current_user.singles_skill,
        'doubles_skill': current_user.doubles_skill,
        'avatar': current_user.avatar,
        'is_verify': current_user.is_verify,
    }), HTTP_201_CREATED