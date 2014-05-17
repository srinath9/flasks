from flask.ext.wtf import Form
from wtforms import TextField, BooleanField , TextAreaField,SubmitField
from wtforms.validators import Required
 
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")

from flask import Flask, render_template,request,redirect

app = Flask(__name__) 
 
app.secret_key = 'development key'

from flask import Flask, render_template, request, flash

from flask.ext.mail import Message, Mail
 
mail = Mail()
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'ksrinathchowdary9@gmail.com'
app.config["MAIL_PASSWORD"] = 'gabbar9347'
 
mail.init_app(app)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('form.html', form=form)
    else:
      template = "<html xmlns='http://www.w3.org/1999/xhtml'><head><h1>soudhdsfudhd</h1>"


      msg = Message(form.subject.data, sender='iota.kodali@gmail.com', recipients=['kodalizzzzz434@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, template)
      mail.send(msg)
 
      return "an,dsmndjnkdsjb"
 
  elif request.method == 'GET':
    return render_template('form.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)


