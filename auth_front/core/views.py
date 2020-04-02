from flask import Blueprint, render_template, redirect, url_for, session, Response
from auth_front.core.forms import ItemForm
from auth_front import auth_api_url
from flask_login import login_required
import requests

core_blueprint = Blueprint('core', __name__)  # , template_folder=(os.path.join(project_dir, '/templates')))


@core_blueprint.route('/home', methods=['GET', 'POST'])
def home():
    form = ItemForm()
    if form.validate_on_submit():
        item = form.item.data
        print(item)
        return redirect(url_for('core.item', item=item))
    return render_template('home.html', form=form)


@core_blueprint.route('/item/<string:item>')
@login_required
def item(item):
    r = requests.get(auth_api_url + '/item/' + item, headers={'api_key': session['user_api_key']})
    return Response(r)


@core_blueprint.route('/items_list')
@login_required
def items_list():
    print('user api key ', session['user_api_key'])
    r = requests.get(auth_api_url + '/items', headers={'api_key': session['user_api_key']})
    return Response(r)
