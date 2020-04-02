import os
from flask import Flask
from flask_login import LoginManager


login_manager = LoginManager()


app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.config['SECRET_KEY'] = 'secretkey'

auth_api_url = "https://auth-app-api.herokuapp.com/"

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from auth_front.core.views import core_blueprint
from auth_front.users.views import users_blueprint


app.register_blueprint(core_blueprint)
app.register_blueprint(users_blueprint)
