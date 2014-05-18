import smtplib
 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import re
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
sender = 'ksrinathchowdary9@gmail.com'
password = 'gabbar9347'
recipient = 'kodalizzzzz434@gmail.com'
subject = 'Python emaillib Test'
message = 'Images attached.'

def main():
    msg = MIMEMultipart()
    msg['Subject'] = 'Python emaillib Test'
    msg['To'] = recipient
    msg['From'] = sender
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)

    path = "/home/srinath/Music/iota/static/metro-vibes-css/images/temp/avatar6.png"
    img = MIMEImage(open(path, 'rb').read(), _subtype="png")
    img.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(img)

  #   part = MIMEText('text', "plain")
 	# part.set_payload(message)
 	
    msg.attach(part)
    session.sendmail(sender, recipient, msg.as_string())
    session.quit()

if __name__ == '__main__':
    main()