import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEText import MIMEText
import os
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
import amazon_emails

smtp_server = 'email-smtp.eu-west-1.amazonaws.com'
smtp_username = 'AKIAJSP64C3S2ZASXBIA'
smtp_password = 'ArcrhJNW+OEiGNoAaHSMKF3Iq8Sqrs44uwR83cGJw8zv'
smtp_port = '587'
smtp_do_tls = True
subject = "sending attachment"
fromEmail = "ksrinathchowdary9@gmail.com"
toEmail = "kodalizzzzz434@gmail.com"
filename = "error.txt"
template = amazon_emails.msg1

def send_message(smtp_server,smtp_username,smtp_password,smtp_port,smtp_do_tls,fromEmail,toEmail,subject,filename,template):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = fromEmail
    body = template
    print filename
    attachment = MIMEText(filename.read())
    attachment.set_payload(filename.read())
    filename.close()
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attachment)
    content = MIMEText(body, 'plain')
    msg.attach(content)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.set_debuglevel(10)
    server.starttls()
    server.ehlo()
    server.login(smtp_username,smtp_password)
    server.sendmail(fromEmail, toEmail, msg.as_string()) 

if __name__ == '__main__':
    send_message(smtp_server,smtp_username,smtp_password,smtp_port,smtp_do_tls,fromEmail,toEmail,subject,filename,template)