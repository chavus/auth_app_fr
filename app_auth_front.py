from auth_front import app
from flask import redirect, url_for


@app.route('/')
def index():
    return redirect(url_for('core.home'))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
