from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def home_page():
    online_users = mongo.db.users.find({'online': True})
    return render_template('index.html',
        online_users=online_users)

@app.route('/user/<username>')
def user_profile(username):
    user = mongo.db.users.find_one_or_404({'_id': username})
    return render_template('user.html',
        user=user)


if __name__ == '__main__':
    app.run()