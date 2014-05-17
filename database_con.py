from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
db = SQLAlchemy()


from flask.ext.mail import Message, Mail
 
mail = Mail()
mail.init_app(app)
app.secret_key = 'development key'

db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:srinath@localhost/flask'
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask.ext.mail import Message, Mail


from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField

class SignupForm(Form):
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Create account")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
   
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

class SigninForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Sign In")
   
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False
     
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'


app.run(debug=True)