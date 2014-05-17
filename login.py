from flask.ext.wtf import Form
from wtforms import TextField, BooleanField , TextAreaField,SubmitField
from wtforms.validators import Required
from flask import Flask, render_template,request
from flask import Flask, render_template, request, flash,redirect
import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from datetime import datetime
from flask.ext.mail import Message, Mail
 

app = Flask(__name__)
app.secret_key = 'development key'

def info(user):

    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    # Get a Database handle to a database named "mydb"
    dbh = c["mydb"]
    assert dbh.connection == c
    users = dbh.side.find({"firstname":user})
    x =users
    
    for no in users:
        print no["email"]
    print "donme"
    return x

@app.route("/")
@app.route("/index")
def index():
	return "nosokdfnlksd"

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")

@app.route('/login', methods = ['GET','POST'])
def login():
	form  = ContactForm()
	if request.method == "POST":
		if form.validate == False:
			return render_template("login.html",form = form,active = True)
		else:
			use = request.form['name']
			x = info(use)
			print use
			print x.count()

      for rod in x:
        print rod['email']


			return render_template("db.html",events =x)
	else:
		return render_template("login.html",form = form, active = False )



if __name__ == "__main__":
	app.run(debug = True)