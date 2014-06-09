from datetime import datetime

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask.ext.stormpath import (
    StormpathError,
    StormpathManager,
    User,
    login_required,
    login_user,
    logout_user,
    user,
)


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'some_really_long_random_string_here'
app.config['STORMPATH_API_KEYFILE'] = 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'My Awesome Application'

stormpath_manager = StormpathManager(app)

if __name__ == '__main__':
    app.run()