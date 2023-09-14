import datetime
import random
import string

from flask import Blueprint, jsonify, request

from ..controllers.registration import new_user

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.get('/otp/create')
def get_otp():
    if not new_user.phone_number:
        return jsonify(), 200

    new_user.registration_otp_expiration = datetime.datetime.now() + datetime.timedelta(seconds=1)
    new_user.registration_otp = create_otp()
    
    return jsonify({
        'OTP': f'{new_user.registration_otp}'
    }), 200


@auth.post('/otp/verify')
def verify_otp(): 
    otp_code = request.json['otp_code']

    if datetime.datetime.now() > new_user.registration_otp_expiration:
        return jsonify({
            'error': 'Expired OTP'
        }), 400
    
    if otp_code != new_user.registration_otp:
        return jsonify({
            'error': 'Invalid OTP'
        }), 400

    return jsonify({
        'user': {
            'phone_number': new_user.phone_number
        }
    }), 200


def create_otp(digits=6):
    otp = ''
    for _ in range(digits):
        otp += random.choice(string.digits)

    return otp