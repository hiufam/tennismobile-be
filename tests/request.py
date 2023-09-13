"""Test requests"""

import time
import requests

BASE = 'http://127.0.0.1:5000/'

new_phone_number = {
    'phone_number': 1231201114,
}

new_user = {
    'full_name': 'pham hieu',
    'date_of_birth': '01/01/2000',
    'gender': 'Male',
    'singles_skill': 2,
    'doubles_skill': 3,
}


response = requests.post(url=BASE + 'api/auth/register/phone-number', json=new_phone_number)


response = requests.get(url=BASE + 'api/auth/otp')

OTP_code = {
    'otp_code': response.json()['OTP']
}

print(response.json()['OTP'])

response = requests.post(url=BASE + 'api/auth/otp', json=OTP_code)

response = requests.post(url=BASE + 'api/auth/register/profile', json=new_user)

print(response.json())