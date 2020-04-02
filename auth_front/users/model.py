from auth_front import login_manager, auth_api_url
from flask import session
from flask_login import UserMixin
import requests


@login_manager.user_loader
def load_user(user_id):
    user_response = requests.get(auth_api_url + '/user',
                                  headers={'api_key': session['user_api_key']})
    if user_response.status_code == 200:
        user_json = user_response.json()
        if int(user_id) == int(user_json['id']):
            user = UserModel(**user_json)
            return user
    return None

class UserModel(UserMixin):

    def __init__(self, id, username, api_key, role):
        self.id = id
        self.username = username
        self.api_key = api_key
        self.role = role

