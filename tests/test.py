"""Test requests"""

import requests

new_user = {
    'phone_number': 12312314,
    'username': 'hieu',
    'dot': '1/1/2000',
    'gender': 'Male,'
}

response = requests.post(url='http://127.0.0.1:5000/' + 'users/1', json=new_user)

print(response.json())