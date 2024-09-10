import requests


def get_user_data():
    response = requests.get('https://api.example.com/user')
    if response.status_code == 200:
        return response.json()
    else:
        return None
