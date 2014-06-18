import smtplib
 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import re
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
sender = 'my@email.com'
password = 'password'
recipient = 'toaddr@email.com'
subject = 'Python emaillib Test'
message = 'Images attached.'
 
directory = "/home/srinath/Music/iota/static/metro-vibes-css/images/temp"
 
def main():
    msg = MIMEMultipart()
    msg['Subject'] = 'Python emaillib Test'
    msg['To'] = recipient
    msg['From'] = sender
 
    files = os.listdir(directory)
    print files
    gifsearch = re.compile(".png", re.IGNORECASE)
    print gifsearch
    files = filter(gifsearch.search, files)
    print files
    for filename in files:
        path = os.path.join(directory, filename)
        print path
        if not os.path.isfile(path):
            print path
            continue
 
        img = MIMEImage(open(path, 'rb').read(), _subtype="png")
        print "img : "
        
        img.add_header('Content-Disposition', 'attachment', filename=filename)
        print img
        msg.attach(img)
 
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
 
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)
 
    session.sendmail(sender, recipient, msg.as_string())
    session.quit()
 
if __name__ == '__main__':
    main()
