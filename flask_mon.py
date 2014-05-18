import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from datetime import datetime
from flask import Flask, render_template,jsonify
from bson import json_util
from bson.objectid import ObjectId
import json
app = Flask(__name__)

def convert(users):
    name= []
    for user in users:
        name.append(user)
        
    
    users = json.dumps(name, default=json_util.default)
    return users


def main():
    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    # Get a Database handle to a database named "mydb"
    dbh = c["mydb"]
    print "done"
    assert dbh.connection == c
    # print dbh.side.find()
    # print "done sdhfgslk"
    name = []
    x =0
    users = dbh.urers.find({"firstname":"Jane"})

    users = convert(users)
    # users = json.dumps(name, default=json_util.default)
    return users

@app.route('/events')
def con():
    notes = main()
    print notes
    return render_template("events.html",events= notes)
    # return notes
def name_event(name):
    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    db = c["mydb"]
    event = db.users.find({"views": 53})
    event = convert(event)
    return event


@app.route('/events/<eventname>')
def events(eventname):
    
    return name_event(eventname)



def register_blueprints(app):
    # Prevents circular imports
    app.register_blueprint(posts)

# register_blueprints(app)
# con()
if __name__ == '__main__':
    app.run(debug=True)



