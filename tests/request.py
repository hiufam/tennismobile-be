"""Test requests"""

import time
import requests

BASE = 'http://127.0.0.1:5000/'

new_phone_number = {
    'phone_number': 1212230114,
}

new_user = {
    'full_name': 'pham hieu',
    'date_of_birth': '01/01/2000',
    'gender': 'Male',
    'singles_skill': 2,
    'doubles_skill': 3,
}

response = requests.post(url=BASE + 'api/registration/phone-number', json=new_phone_number)

response = requests.get(url=BASE + 'api/auth/otp/create')

otp = response.json()['OTP']

print(otp)

my_otp = {
    'otp_code': otp
}

# time.sleep(2)

response = requests.post(url=BASE + 'api/auth/otp/verify', json=my_otp)

print(response.json())