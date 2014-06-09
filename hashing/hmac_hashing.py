import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from datetime import datetime
from flask import Flask, render_template,jsonify
from bson import json_util
from bson.objectid import ObjectId
import json
from flask_hmac import Hmac
app = Flask(__name__)
app.config['HMAC_KEY']="srinath"
app.config['HMAC_DISARM']="srinivas"

hm = Hmac(app)


@app.route('/login', methods = ['GET','POST'])
@hm.check_hmac
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