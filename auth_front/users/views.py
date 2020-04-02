from flask import Blueprint, render_template, flash, url_for, redirect, request, session
from flask_login import login_user, login_required, logout_user
from auth_front.users.forms import RegistrationForm, LoginForm
from auth_front.users.model import UserModel
from auth_front import auth_api_url
import requests


users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_pwd = {"username": form.username.data, "password": form.password.data}
        requests.post(auth_api_url + '/register', data=user_pwd)
        flash('User registered successfully')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_pwd = {"username": form.username.data, "password": form.password.data}
        user_response = requests.post(auth_api_url + '/auth', data=user_pwd)
        if user_response.status_code == 200:
            user_json = user_response.json()
            auth_user = UserModel(**user_json)
            login_user(auth_user)
            session['user_api_key'] = auth_user.api_key
            flash('You are now logged in!')
            next = request.args.get('next')    # in case login is required when trying to enter another page. It will be saved at "next" and redirect after login
            if not next:
                next = url_for('core.home')    # if there were no page, send to home
            return redirect(next)
        else:
            flash('Incorrect credentials')

    return render_template('login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('user_api_key', None)
    flash('You are now logged out!')
    return redirect(url_for('core.home'))







